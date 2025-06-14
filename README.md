# Stock Market Prediction using Machine Learning

# Stock Market Prediction

This repository contains a Stock Market Prediction application that leverages machine learning models and analyses to forecast market trends. The project is composed of multiple modules including data preprocessing, model training, prediction interfaces, and a user authentication system.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Base](#data-base)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

---

## Overview

The Stock Market Prediction application leverages historical financial data and cutting-edge algorithms to forecast market movements. The repository includes scripts for data extraction, processing, and visualization along with a database to manage user logins and prediction history.

---

## Features

- User authentication with secure login
- Prediction history tracking
- MySQL database integration for data persistence
- Modular code structure for ease of development and contribution
- Well-documented code for easy understanding and maintainability

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ShubhamShaw01/StockMarketPrediction.git
   cd StockMarketPrediction
   ```

2. **Set Up Your Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use: venv\Scripts\activate
   ```

3. **Install the Required Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file (or update your environment variables) with your database credentials and other configuration parameters.

---

### To run app using Dockerfile


1. **Navigate to your project directory**

   ``` bash
   cd /path/to/your/project
   ```
2. **Build the Docker image**

   ``` bash
   docker build -t your-image-name .
   ```
   eg: docker build -t stockmarketprediction .

3. **Verify the image was built**

   ``` bash
   docker images
   ```
4. **Run the Docker container**

   ``` bash
   docker run -p host-port:container-port your-image-name
   ```

   eg: docker run -p 8501:8501 stockmarketprediction
## Usage

After installation, you can run the application using:

```bash
python main.py
```

The application will start and provide necessary logs and instructions in the terminal.

---

## Data Base

The application uses a MySQL database to store user credentials and prediction histories. Please follow these steps to set up your database:

1. **Configure Your Database Connection**

   In your application, use the following code snippet to connect to your MySQL database:

   ```python
   import pymysql as mysql

   connection = mysql.connect(
       host="provide your host name, eg='localhost'",
       port="provide your port id, eg=3306",
       user="provide your name, eg='root'",
       password="provide your password, eg='1234'",
       database="provide your database name, eg='stock_database'"
   )
   ```

2. **Run the Following SQL Script**

   Execute the following SQL script in your MySQL Workbench to create the necessary tables for the application:

   ```sql
   CREATE TABLE userlogin (
       userName VARCHAR(20) NOT NULL PRIMARY KEY,
       userPassword VARCHAR(255) NOT NULL
   );

   CREATE TABLE history (
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(255) NOT NULL,
       company_name VARCHAR(255) NOT NULL,
       company_ticker VARCHAR(10) NOT NULL,
       investment_amount DECIMAL(15,2) NOT NULL,
       final_value DECIMAL(15,2) NOT NULL,
       total_profit DECIMAL(15,2) NOT NULL,
       timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

   This script creates a table for user login details and another for recording transaction history, including the company details and profit metrics.

---

## Thumbnail

Below is the thumbnail image for the project:

![Project Thumbnail](https://github.com/user-attachments/assets/b3db569c-6bda-47d2-a872-1de6a1403e12)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with detailed explanations of your modifications. Ensure that your contributions are well documented and tested.

---

## Contact

For any questions or feedback, please contact:

- **Shubham Shaw** - [GitHub Profile](https://github.com/ShubhamShaw01)
