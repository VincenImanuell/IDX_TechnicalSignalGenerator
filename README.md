# IDX Technical Signal Generator

Simple Python project to generate `BUY`, `SELL`, or `HOLD` signals for Indonesian stocks (IDX) using moving average crossover and RSI logic.

## Features
- Downloads historical price data from Yahoo Finance via `yfinance`
- Automatically maps ticker input to IDX format (for example `BBCA` -> `BBCA.JK`)
- Calculates:
  - `MA20` (20-day moving average)
  - `MA50` (50-day moving average)
  - `RSI14` (14-day Relative Strength Index)
- Generates signals:
  - `BUY` when `MA20 > MA50`
  - `SELL` when `MA20 < MA50`
  - `BUY` when `RSI14 < 30` (oversold)
  - `SELL` when `RSI14 > 70` (overbought)
  - `HOLD` otherwise
- Generates final signal (`MA + RSI`) with conflict handling:
  - Same direction (`BUY`/`SELL`) -> follow that signal
  - One indicator `HOLD` -> follow the other indicator
  - Conflict (`BUY` vs `SELL`) -> `HOLD`
- Provides explanations for each result:
  - `MA Reason`
  - `RSI Reason`
  - `Final Reason`

## Project Structure
```text
IDX_TechnicalSignalGenerator/
|-- main.py
|-- indicators/
|   `-- moving_average.py
|   `-- rsi.py
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
IDX Technical Signal Generator
Method: MA20/MA50 crossover + RSI14 (30/70)
Final signal combines MA and RSI.
Stock ticker (BBCA, BBRI, etc): BBCA
MA Signal: BUY
MA Reason: MA20 (9480.25) is above MA50 (9320.80).
RSI Signal: HOLD
RSI Reason: RSI14 (54.21) is between 30-70 (neutral).
Trading Signal (MA + RSI): BUY
Final Reason: RSI is neutral, following MA: BUY. MA20 (9480.25) is above MA50 (9320.80). RSI14 (54.21) is between 30-70 (neutral).
```

## Signal Logic
The app computes indicators on close prices:
- `MA20 = rolling mean of Close over 20 days`
- `MA50 = rolling mean of Close over 50 days`
- `RSI14 = Relative Strength Index over 14 periods`

Then it generates per-indicator signals:
- `MA20 > MA50` -> `BUY`
- `MA20 < MA50` -> `SELL`
- `RSI14 < 30` -> `BUY`
- `RSI14 > 70` -> `SELL`
- otherwise or insufficient valid data -> `HOLD`

It also generates human-readable reasons from the latest indicator values.

Final `Trading Signal (MA + RSI)`:
- same MA and RSI direction -> `BUY`/`SELL`
- if one side is `HOLD`, use the other side
- opposite MA and RSI directions -> `HOLD`

## Notes
- This project is for educational use, not financial advice.
- Market data availability depends on Yahoo Finance and your local environment/network.
