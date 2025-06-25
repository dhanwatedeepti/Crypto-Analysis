# Crypto-Analysis
📊 Live Crypto Data in Excel This project automatically fetches and updates the top 50 cryptocurrency prices in an Excel sheet every 5 minutes! Built using Python, Pandas, and OpenPyXL, it analyzes: ✔️ Top 5 cryptocurrencies by market cap. ✔️ Price trends &amp; 24-hour changes. ✔️ Live data tracking for easy monitoring.
# 📊 Live Cryptocurrency Price Tracker in Excel

A Python-based automation project that **fetches live cryptocurrency data** from an online API and updates an **Excel sheet every 5 minutes**. This project is ideal for crypto enthusiasts, data analysts, and developers who want **automated real-time monitoring** without the need for a web interface.

---

## 🚀 Features

- ✅ Fetches **top 50 cryptocurrencies** using a public API
- ✅ Tracks:
  - Name, Symbol, Rank
  - Current Price
  - 24h Price Change %
  - Market Cap
  - Timestamp
- ✅ Highlights the **Top 5 coins by market cap**
- ✅ Automatically updates **every 5 minutes**
- ✅ Saves the data in a well-formatted Excel sheet
- ✅ No frontend or GUI required – runs purely in Python

---

## 🛠️ Tech Stack

- 🐍 **Python**
- 📦 `pandas` – for data handling
- 📦 `requests` – to fetch API data
- 📦 `openpyxl` – to work with Excel files
- ⏱️ `time` – for timed updates

---

## 🧪 How It Works

1. Sends a request to a **cryptocurrency API** (like CoinGecko or CoinMarketCap)
2. Parses the JSON response and extracts the top 50 cryptocurrencies
3. Sorts and highlights the **Top 5** based on market cap
4. Saves the data into `crypto_data.xlsx` with:
   - Proper formatting
   - Timestamp
5. Repeats the process every **5 minutes**

