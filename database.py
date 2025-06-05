import pymysql as mysql
import pandas as pd
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

timeout = 5  # seconds

def get_db_connection():
    try:
        connection = mysql.connect(
            charset="utf8mb4",
            connect_timeout=timeout,
            cursorclass=mysql.cursors.DictCursor,
            database=os.getenv("DB_NAME"),
            host=os.getenv("DB_HOST"),
            password=os.getenv("DB_PASSWORD"),
            read_timeout=timeout,
            port=int(os.getenv("DB_PORT", "12564")),
            user=os.getenv("DB_USER"),
            write_timeout=timeout,
        )
        return connection
    except Exception as e:
        st.error(f"Connection error: {e}")
        st.stop()

def authenticate_user(username, password):
    username = username.strip().lower()
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM userlogin WHERE userName=%s AND userPassword=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        # result is a dict because of DictCursor, get the first value
        count = list(result.values())[0] if result else 0
        return count == 1
    except Exception as e:
        st.error(f"Authentication error: {e}")
        return False
    finally:
        conn.close()

def register_user(username, password):
    username = username.strip().lower()
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM userlogin WHERE userName=%s", (username,))
        result = cursor.fetchone()
        count = list(result.values())[0] if isinstance(result, dict) else result[0]

        if count > 0:
            st.warning("Username already exists.")
            return False

        cursor.execute("INSERT INTO userlogin (userName, userPassword) VALUES (%s, %s)", (username, password))
        conn.commit()
        st.success("Account created! Please log in.")
        return True
    except Exception as e:
        st.error(f"Registration error: {e}")
        return False
    finally:
        conn.close()

def insert_history(username, company_name, company_ticker, investment_amount, final_value, total_profit):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            query = """
            INSERT INTO history (username, company_name, company_ticker, investment_amount, final_value, total_profit)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (username, company_name, company_ticker, investment_amount, final_value, total_profit))
            connection.commit()
            st.success("Transaction history saved successfully.")
        except mysql.MySQLError as err:
            st.error(f"Error saving transaction: {err}")
        finally:
            cursor.close()
            connection.close()

def seek_history(username):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            query = """
            SELECT username, company_name, company_ticker, investment_amount, final_value, total_profit, timestamp
            FROM history
            WHERE username = %s
            ORDER BY id DESC
            """
            cursor.execute(query, (username,))
            history_data = cursor.fetchall()
            if history_data:
                df_history = pd.DataFrame(history_data)
                # Optionally format column names for display
                df_history.columns = [
                    "Username", "Company Name", "Company Ticker",
                    "Investment Amount", "Final Value", "Total Profit", "Transaction Date"
                ]
                # Format numbers for better readability
                df_history["Investment Amount"] = df_history["Investment Amount"].apply(lambda x: f"₹{x:,.2f}")
                df_history["Final Value"] = df_history["Final Value"].apply(lambda x: f"₹{x:,.2f}")
                df_history["Total Profit"] = df_history["Total Profit"].apply(lambda x: f"₹{x:,.2f}")
                st.dataframe(df_history)
            else:
                st.warning("No history found.")
        except mysql.MySQLError as err:
            st.error(f"Error fetching transaction history: {err}")
        finally:
            cursor.close()
            connection.close()