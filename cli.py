# cli.py
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker-file", required=True, help="File containing list of tickers")
    parser.add_argument("--start-date", required=True, help="Start date in YYYY-MM-DD format")
    parser.add_argument("--end-date", required=True, help="End date in YYYY-MM-DD format")
    parser.add_argument("--output-dir", default=".", help="Directory to save output CSV files")
    args = parser.parse_args()
    return args