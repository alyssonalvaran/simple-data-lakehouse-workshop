# Data-Engineered Analytics: Building Schema-Driven Event Pipelines in Python

Software applications often emit event logs as flexible, unstructured JSON payloads. While this speeds up initial feature development, it creates a massive gap when downstream analytics systems require rigid, predictable tables. 

This workshop repository provides a hands-on, self-contained project for building a modern "Data Lakehouse" pipeline using **Python**, **Pydantic**, **DuckDB**, and **Streamlit**. You will learn how to bridge the disconnect by ingesting synthetic JSON streams, enforcing strict schemas, exporting clean data to **Parquet**, and serving it to an interactive dashboard—all with zero infrastructure overhead.

## What You Will Learn

* **Event Simulation:** Programmatically generate continuous, realistic mock data streams using Faker to safely test pipeline resilience and data drift.
* **Schema Enforcement & Error Isolation:** Use Pydantic to validate messy JSON event payloads, enforce strict data contracts, and gracefully isolate malformed records without crashing the ingestion process.
* **Pipeline Architecture:** Build a clean, modular Python script that reads streaming raw logs, normalizes them, and preps them for analytics.
* **Data Lakehouse Architecture:** Export validated records into Apache Parquet files for highly compressed storage, and use DuckDB as a lightning-fast engine to query them directly with SQL.
* **Dashboard Visualization:** Connect an in-memory DuckDB engine to a Streamlit application to build metrics and charts on the fly.

---

## Prerequisites

* **Python 3.10+** installed on your machine.
* A basic understanding of Python (dictionaries, classes/dataclasses, and functions).
* Familiarity with basic SQL queries (`SELECT`, `GROUP BY`, `JOIN`).

---

## Project Structure

```text
simple-data-lakehouse/
├── data/
│   ├── raw_events_*.json      # Generated synthetic JSON event payloads (streamed)
│   └── analytics.parquet      # Exported Parquet file for the dashboard
├── models/
│   └── events.py              # Pydantic schemas for event validation
├── dashboard.py               # Streamlit application for data visualization
├── generate_data.py           # Script to generate realistic mock data with Faker
├── pipeline.py                # Main ingestion and transformation script
├── requirements.txt           # Project dependencies
└── README.md
```

## Getting Started

### 1. Clone the Repository

```bash
git clone [https://github.com/alyssonalvaran/simple-data-lakehouse](https://github.com/alyssonalvaran/simple-data-lakehouse)
cd simple-data-lakehouse
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate Synthetic Data

Run the generator script to simulate a live stream of realistic mock event logs. The script will continuously generate new JSON files in the `data/` directory every 5 seconds. This intentionally injects a controlled error rate to test the pipeline's validation logic.

Leave this running in a separate terminal:

```bash
python generate_data.py
```
*(Press `Ctrl+C` when you want to stop the stream)*

### 5. Run the Pipeline

Execute the main script to process all the generated JSON logs in the `data/` directory, drop malformed records, and load the clean data into DuckDB for analytics:

```bash
python pipeline.py
```

### 6. Run the Dashboard

Spin up a real-time Streamlit dashboard to visualize the data in your DuckDB file:

```bash
streamlit run dashboard.py
```

---

## Workshop Outline

This hands-on session is structured into five progressive modules, designed to take participants from messy input data to query-ready analytics:

* **Module 1: The Problem with Unstructured JSON**
  * Understanding the friction between flexible application logs and rigid analytical data requirements.
  * Examining sample raw payloads and identifying common data drift and corruption issues.

* **Module 2: Schema Enforcement with Pydantic**
  * Introduction to data contracts and validation in Python.
  * Writing Pydantic models to enforce strict types, field constraints, and custom validators.
  * Handling validation errors gracefully without breaking the ingestion pipeline.

* **Module 3: Building the Local Pipeline**
  * Designing a modular Python script to read, validate, and transform raw JSON logs.
  * Preparing normalized data structures ready for analytical storage.

* **Module 4: Exporting and Analytics with DuckDB**
  * Using an embedded DuckDB instance to export validated data into Apache Parquet format.
  * Writing analytical SQL queries to read directly from the Parquet files.

* **Module 5: Visualization with Streamlit**
  * Connecting DuckDB to a Streamlit application and querying Parquet files on the fly.
  * Building interactive metrics, charts, and data tables to visualize the clean event data.

## Next Steps

Finished the core workshop? Here are a few ways you can extend the project and take your skills further:

* **Automate with Cron or Airflow:** Turn the static python script into a scheduled pipeline that runs hourly or daily against a live event stream.
* **Production Storage (State & Evolution):** Make your pipeline production-ready by moving processed JSON files into an `archive/` folder to prevent duplicates, saving multiple partitioned Parquet files over time, and querying them seamlessly using DuckDB's `read_parquet('data/*.parquet', union_by_name=True)`.
* **Implement Error Dead-Letter Queues:** Instead of dropping or crashing on invalid Pydantic payloads, route failing records into a separate `error_log.json` file for debugging and schema evolution tracking.
* **Scale to MotherDuck:** Swap your in-memory DuckDB connection for a MotherDuck cloud connection to see how your dashboard can transition to a hybrid cloud environment.
* **Advanced Dashboarding:** Expand your `dashboard.py` Streamlit app to include date filters, auto-refresh features, or more complex Altair visualizations.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/alyssonalvaran/simple-data-lakehouse/blob/main/LICENSE) file for details.
