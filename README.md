# Stock Market Prediction using Machine Learning

## Overview
This project aims to predict stock market trends using machine learning techniques. It involves data collection, preprocessing, feature engineering, model training, and evaluation to generate accurate predictions of stock prices or trends.

## Features
- Data collection from stock market sources (Yahoo Finance, Alpha Vantage, etc.)
- Data preprocessing (handling missing values, normalization, feature selection)
- Feature engineering (technical indicators, sentiment analysis, etc.)
- Model training using various machine learning algorithms
- Model evaluation and performance analysis
- Visualization of stock trends and predictions

## Technologies Used
- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, TensorFlow/Keras, Matplotlib
- **Data Source**: Yahoo Finance APIs
- **Model Types**: LSTM

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ShubhamShaw01/StockMarketPrediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd stock-market-prediction
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the data collection script:
   ```bash
   python data_collection.py
   ```
2. Preprocess the data:
   ```bash
   python preprocess_data.py
   ```
3. Train the model:
   ```bash
   python train_model.py
   ```
4. Evaluate the model:
   ```bash
   python evaluate_model.py
   ```
5. Make predictions:
   ```bash
   python predict.py
   ```

## Results and Evaluation
- Model performance is evaluated using metrics like RMSE, MAE, and R-squared.
- Visualization of actual vs. predicted prices.
- Comparative analysis of different ML models.

## Future Enhancements
- Incorporation of deep learning models (LSTMs, transformers)
- Real-time stock prediction
- Sentiment analysis of news headlines affecting stocks

## Data Base
connection = mysql.connect(
            host= provide your host name, eg="localhost"
            port=provide your port id , eg=3306
            user=provide yours name, eg="root"
            password=provide your password, eg="1234"
            database=provide your database naem, eg="stock_database"
        )
   ### run this script in your mysql workbench for application to work
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


## Contributing
Feel free to fork this repository and submit pull requests for improvements!

## Contact
For any queries, reach out to **Shubham Shaw** at [sshaw1324@gmail.com].

![Thumbnail](https://github.com/user-attachments/assets/d0581f07-2e02-484d-8f3a-cf786403bbd8)
