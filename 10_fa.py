import subprocess

scripts = ['06_fa.py', '07_fa.py', '08_fa.py', '09_fa.py']

for script in scripts:
    subprocess.run(['python', script, '--ticker-file', 'tickers.txt', '--start-date', '2023-01-01', '--end-date', '2023-12-31', '--output-dir', 'data'])