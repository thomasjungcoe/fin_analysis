from cli import parse_args
import yfinance as yf
import os

def download_data(symbol, start_date, end_date, output_dir, freq=None, suffix='D'):
    data = yf.download(symbol, start=start_date, end=end_date, interval= "1D")
    if freq is not None:
        data = data.resample(freq).first()
        dat = data.bfill()
    data = data.drop(['Volume'], axis=1)
    data.to_csv(os.path.join(output_dir, f'US-{symbol}-{suffix}.csv'))


def main():
    args = parse_args()

    with open(args.ticker_file, 'r') as f:
        tickers = [line.strip() for line in f]

    for ticker in tickers:
        download_data(ticker, args.start_date, args.end_date, args.output_dir)
        download_data(ticker, args.start_date, args.end_date, args.output_dir, 'W', 'W')
        download_data(ticker, args.start_date, args.end_date, args.output_dir, 'MS', 'M')
        download_data(ticker, args.start_date, args.end_date, args.output_dir, 'QS', 'Q')


if __name__ == "__main__":
    main()