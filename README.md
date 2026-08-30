## VERSION
**📈 TrendPulse v1.0**

TrendPulse is a Python-based live cryptocurrency trend tracker that collects trending coin data from the **CoinGecko API**, processes and analyzes it using **pandas**, and visualizes 24-hour price movements using **Matplotlib**.

The project was built as a mini data pipeline to understand how live data can be collected from an API, transformed into a structured dataset, analyzed, and presented through visualization.

---

## 🚀 Features

* Fetches live trending cryptocurrency data from the CoinGecko API
* Handles API request errors using `try/except`
* Converts API JSON data into a structured pandas DataFrame
* Processes and cleans numerical data
* Identifies:

  * 🔥 Top gainer
  * 📉 Top loser
  * 💰 Highest market-cap coin
  * 📊 Average 24-hour price change
* Visualizes positive and negative price movements
* Uses different colors for gains and losses
* Automatically refreshes the visualization every 60 seconds
* Displays the last successful update time
* Stops cleanly when the visualization window is closed

---

## 🏗️ Project Structure

```text
Trendpulse-Muneer/
│
├── README.md
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_data_analysis.py
└── task4_visualization.py
```

### Task 1 — Data Collection

`task1_data_collection.py`

Responsible for:

* Sending a GET request to the CoinGecko API
* Checking the HTTP response
* Handling request failures
* Extracting the required cryptocurrency information
* Returning the collected data

### Task 2 — Data Processing

`task2_data_processing.py`

Responsible for:

* Converting the collected data into a pandas DataFrame
* Selecting relevant columns
* Converting values to appropriate data types
* Preparing the data for analysis and visualization

### Task 3 — Data Analysis

`task3_data_analysis.py`

Responsible for extracting useful insights from the processed DataFrame, including:

* Top gainer
* Top loser
* Highest market capitalization
* Average 24-hour price change

### Task 4 — Visualization

`task4_visualization.py`

Responsible for:

* Creating the live visualization
* Displaying positive and negative price changes
* Adding percentage labels
* Showing the zero reference line
* Displaying the last update time
* Refreshing the chart automatically

---

## 🔄 Data Pipeline

```text
CoinGecko API
      ↓
Data Collection
      ↓
Data Processing
      ↓
Data Analysis
      ↓
Data Visualization
      ↓
Live TrendPulse Chart
```

The visualization refreshes periodically so that the tracker can display newly fetched trending data.

---

## 🛠️ Technologies Used

* **Python**
* **Requests** — HTTP requests to the API
* **pandas** — data processing and analysis
* **Matplotlib** — data visualization
* **CoinGecko API** — live cryptocurrency data
* **Git & GitHub** — version control

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Muneer-2005/Trendpulse-Muneer.git
```

### 2. Navigate into the project

```bash
cd Trendpulse-Muneer
```

### 3. Install the required libraries

```bash
pip install requests pandas matplotlib
```

### 4. Run the visualization

```bash
python task4_visualization.py
```

TrendPulse will fetch the latest trending data and display the visualization.

The chart automatically refreshes every 60 seconds.

To stop the tracker, close the visualization window.

---

## 📊 Example Insights

TrendPulse can identify information such as:

```text
Top Gainer:       Helium
Top Loser:        Chump Coin
Highest Market Cap: Bitcoin
Average 24h Change: ...
```

The actual results change because the project uses live API data.

---

## 🎯 Learning Objectives

This project was created to practice the fundamentals of a real-world data pipeline:

1. Working with REST APIs
2. Sending HTTP GET requests
3. Handling API responses and errors
4. Working with JSON data
5. Converting raw data into pandas DataFrames
6. Performing exploratory analysis with pandas
7. Using `idxmax()`, `idxmin()`, `loc()`, and aggregation functions
8. Creating meaningful data visualizations
9. Building a simple live data tracker
10. Organizing a project into modular Python scripts
11. Using Git and GitHub for version control

---

## 🔮 Future Improvements

Possible future improvements include:

* Store historical API results in a database
* Track price changes over time
* Add interactive charts
* Add more cryptocurrency metrics
* Build a Streamlit dashboard
* Add additional data sources
* Add historical trend analysis

---

## 📌 Note

TrendPulse is an educational mini project created to demonstrate API-based data collection, processing, analysis, and visualization.

Cryptocurrency data is retrieved from CoinGecko and can change between refreshes.