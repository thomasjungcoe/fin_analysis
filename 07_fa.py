import argparse
import yfinance as yf
import os

def download_data(symbol, start_date, end_date, output_dir):
    data = yf.download(symbol, start=start_date, end=end_date, interval= "1wk")
    data = data.drop(['Volume'], axis=1)
    data.to_csv(os.path.join(output_dir, f'US-{symbol}-W.csv'))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker-file", required=True, help="File containing list of tickers")
    parser.add_argument("--start-date", required=True, help="Start datae in YYYY-MM-DD format")
    parser.add_argument("--end-date", required=True, help="End date in YYYY-MM-DD format")
    parser.add_argument("--output-dir", default=".", help="Directory to save output CSV files")
    args = parser.parse_args()

    with open(args.ticker_file, 'r') as f:
        tickers = [line.strip() for line in f]

    for ticker in tickers:
        download_data(ticker, args.start_date, args.end_date, args.output_dir)


if __name__ == "__main__":
    main()