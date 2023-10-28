import yfinance as yf

# Define the ticker symbol
ticker_symbol = "amzn"

# Define the date range for historical data
start_date = "2022-01-01"
end_date = "2022-10-31"

# Fetch historical data using yfinance
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Display the retrieved data
print(data)
