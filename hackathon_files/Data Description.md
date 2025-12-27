# Data Description

This dataset provides daily environmental context for the
Symptom Detective Agent focused on chronic respiratory illness.

## Data Sources
- Air Quality Index (AQI): Simulated (OpenAQ-compatible format)
- PM2.5 concentration: Simulated values
- Weather data: Daily temperature and humidity

## Features
- date: Calendar date (YYYY-MM-DD)
- aqi: Overall air quality index
- pm25: Particulate matter PM2.5 concentration
- temperature: Daily average temperature (°C)
- humidity: Daily average relative humidity (%)
- location: City name

## Usage
The agent uses this dataset to:
- Analyze delayed effects of AQI exposure (1–5 day lag)
- Generate hypotheses about environmental respiratory triggers
- Support explainable, non-diagnostic reasoning
