# TrendPulse

A Python mini data pipeline that retrieves live trending cryptocurrency data from the CoinGecko API, processes it with pandas, calculates simple market insights, and visualizes 24-hour price changes with Matplotlib.

> **Project type:** Academic / learning project

## Pipeline

```text
CoinGecko API
     ↓
Data collection
     ↓
Data processing
     ↓
Analysis
     ↓
Visualization
```

## Features

- Fetches trending cryptocurrency data from CoinGecko
- Handles HTTP/request failures
- Converts API JSON into a pandas DataFrame
- Cleans numeric market-cap and volume fields
- Finds the top 24-hour gainer and loser
- Finds the highest market-cap coin
- Calculates average 24-hour price change
- Displays a Matplotlib bar chart
- Refreshes the chart periodically

## Repository structure

```text
Trendpulse-Muneer/
├── README.md
├── requirements.txt
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_analysis.py
└── task4_visualization.py
```

### Module responsibilities

**`task1_data_collection.py`**
Retrieves and normalizes the fields needed by the rest of the pipeline.

**`task2_data_processing.py`**
Builds the DataFrame and converts market-cap/volume strings to numeric values.

**`task3_analysis.py`**
Calculates the top gainer, top loser, highest market cap, and average 24-hour change.

**`task4_visualization.py`**
Combines the pipeline and displays the live visualization.

## Setup

Python 3.x is required.

```bash
git clone https://github.com/Muneer148/Trendpulse-Muneer.git
cd Trendpulse-Muneer
pip install -r requirements.txt
```

Run:

```bash
python task4_visualization.py
```

The application requires internet access because the data comes from the CoinGecko API.

## Important note

Cryptocurrency values are live and can change between requests. The project is for learning API integration, data processing, analysis, and visualization; it is **not financial advice or a trading system**.

## Possible next improvements

- Add retry/backoff handling
- Store historical observations
- Add tests for the processing and analysis functions
- Separate data fetching from visualization timing
- Add interactive charts or a dashboard
- Add configurable refresh intervals

## Author

**Shaik Muneeruddin**
