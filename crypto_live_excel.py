import requests
import pandas as pd
import time
from openpyxl import load_workbook

# CoinGecko API URL
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1,
    "sparkline": False
}

EXCEL_FILE = "crypto_data.xlsx"
SHEET_NAME = "Live Data"

# Function to fetch cryptocurrency data
def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data", response.status_code)
        return None

# Function to process and analyze data
def process_data(data):
    df = pd.DataFrame(data)[["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]]
    df.columns = ["Name", "Symbol", "Price (USD)", "Market Cap", "24h Volume", "24h Change (%)"]
    
    # Analysis
    top_5 = df.nlargest(5, "Market Cap")
    avg_price = df["Price (USD)"].mean()
    max_change = df["24h Change (%)"].max()
    min_change = df["24h Change (%)"].min()
    
    return df, top_5, avg_price, max_change, min_change

# Function to save data to Excel
def save_to_excel(df):
    try:
        with pd.ExcelWriter(EXCEL_FILE, mode="w", engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name=SHEET_NAME, index=False)
    except Exception as e:
        print("Error writing to Excel:", e)

# Main function to run every 5 minutes
def main():
    while True:
        print("Fetching latest data...")
        data = fetch_crypto_data()
        if data:
            df, top_5, avg_price, max_change, min_change = process_data(data)
            save_to_excel(df)
            print("Data updated in Excel.")
            print(f"Top 5 Cryptos by Market Cap:\n{top_5}\n")
            print(f"Average Price: ${avg_price:.2f}")
            print(f"Highest 24h Change: {max_change:.2f}%")
            print(f"Lowest 24h Change: {min_change:.2f}%")
        print("Waiting for next update (5 mins)...")
        time.sleep(300)  # Wait 5 minutes

if __name__ == "__main__":
    main()
