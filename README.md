# IDX Technical Signal Generator

Simple Python project to generate `BUY`, `SELL`, or `HOLD` signals for Indonesian stocks (IDX) using moving average crossover logic.

## Features
- Downloads historical price data from Yahoo Finance via `yfinance`
- Automatically maps ticker input to IDX format (for example `BBCA` -> `BBCA.JK`)
- Calculates:
  - `MA20` (20-day moving average)
  - `MA50` (50-day moving average)
- Generates signal:
  - `BUY` when `MA20 > MA50`
  - `SELL` when `MA20 < MA50`
  - `HOLD` otherwise

## Project Structure
```text
IDX_TechnicalSignalGenerator/
|-- main.py
|-- indicators/
|   `-- moving_average.py
|-- signals/
|   `-- signal_generator.py
|-- utils/
|   `-- data_loader.py
|-- requirements.txt
`-- README.md
```

## Requirements
- Python 3.10+ recommended
- Dependencies listed in `requirements.txt`

## Installation
```bash
pip install -r requirements.txt
```

## Usage
Run:

```bash
python main.py
```

Input ticker without `.JK`, for example:
- `BBCA`
- `BBRI`
- `TLKM`

Example output:
```text
Stock ticker (BBCA, BBRI, etc): BBCA
Trading Signal: HOLD
```

## Signal Logic
The app computes moving averages on close prices:
- `MA20 = rolling mean of Close over 20 days`
- `MA50 = rolling mean of Close over 50 days`

Then it compares the latest valid values:
- `MA20 > MA50` -> `BUY`
- `MA20 < MA50` -> `SELL`
- equal or insufficient valid data -> `HOLD`

## Notes
- This project is for educational use, not financial advice.
- Market data availability depends on Yahoo Finance and your local environment/network.
