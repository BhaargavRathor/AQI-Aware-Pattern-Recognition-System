# AQI AWARE PATTERN RECOGNITION SYSTEM


## Symptom Detective Agent for Respiratory Health

This project presents an agentic system designed to identify patterns
between air quality trends (AQI) and respiratory symptom flare-ups.
The system reasons over delayed effects of pollution exposure and provides
explainable, non-clinical insights for awareness and self-management.

Rising air pollution levels in cities like Delhi and other Indian states
have led to a significant increase in respiratory issues. This system aims to
help users understand how worsening AQI may be contributing to their symptoms
over time.

## Project Structure
hackathon_files/


├── agent_definition.md # Agent goals, scope, and constraints
├── agent_reasoning.md # Agent reasoning loop and logic
├── pseudocode.md # Step-by-step agent pseudocode
├── codereasoning.py # Core agent reasoning implementation
├── data_ingestion.py # AQI and environmental data handling
├── sample_data.csv # Example dataset
├── synthetic_city_3000_rows.csv


## How to Run the Project (Demo)

1. Clone the repository:

https://github.com/BhaargavRathor/AQI-Aware-Pattern-Recognition-System.git

2. Navigate to the project folder:

cd AQI-Aware-Pattern-Recognition-System/hackathon_files

3.Run the agent reasoning script:
python codereasoning.py


The agent simulates respiratory symptom analysis and explains how AQI trends
may contribute to symptom flare-ups using delayed temporal reasoning.

#HOW TO USE THE DEMO WEBPAGE
1.We upload the file synthetic_city_3000_rows.csv file
It contains the data for Delhi as demo.




## Key Features
- AQI-aware temporal reasoning (1–5 day delay windows)
- Adaptive trigger confidence updates
- Explainable agentic behavior
- Long-term memory of symptoms and AQI trends
- Non-diagnostic, awareness-focused design



## Agentic Design Overview
The system follows an **observe–reason–adapt** loop:
- Observes respiratory symptoms and AQI data
- Reasons over delayed environmental effects
- Generates and updates trigger hypotheses
- Adapts confidence based on observed outcomes

This distinguishes the system from static analytics or prediction models.



## Ethics & Disclaimer
This system does **not** provide medical diagnosis, treatment, or clinical
recommendations. All outputs are probabilistic and intended strictly for
**educational and awareness purposes**.



## Demo Video
A short demo video explaining the system and its agentic behavior is provided
via the YouTube link in the submission form.













