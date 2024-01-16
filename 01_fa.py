import argparse
import yfinance as yf
import os

def download_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date, interval= "1d")
    return data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True, help="Symbol to download data for")
    parser.add_argument("--start-date", required=True, help="Start datae in YYYY-MM-DD format")
    parser.add_argument("--end-date", required=True, help="End date in YYYY-MM-DD format")
    parser.add_argument("--output", default="C:/Users/thoma/Desktop/fin_analysis/data", help="Path to output CSV file")
    args = parser.parse_args()


    data = download_data(args.symbol, args.start_date, args.end_date)
    data.to_csv(args.output)

if __name__ == "__main__":
    main()