AGENT GOAL:
Identify environmental triggers (especially poor AQI) that increase
respiratory symptom severity over time.

INITIALIZE:
- symptom_history = empty list
- environmental_history = empty list
- trigger_confidence = dictionary
    AQI_trigger = 0.5
    Humidity_trigger = 0.5
    Outdoor_exposure_trigger = 0.5



FOR each new day:

1. OBSERVE
   - Read today's symptom severity (0 to 3)
   - Read today's AQI, PM2.5, PM10
   - Read today's humidity and temperature
   - Read outdoor exposure (yes/no)

2. STORE
   - Append today’s data to symptom_history
   - Append today’s data to environmental_history

3. CHECK FOR SYMPTOM FLARE
   IF today’s symptom severity > yesterday’s severity:

       4. TEMPORAL ANALYSIS
          - Look at AQI values from past 1 to 5 days
          - Calculate average AQI during that window

       5. HYPOTHESIS UPDATE
          IF average AQI > safe threshold:
              Increase AQI_trigger confidence
          ELSE:
              Slightly decrease AQI_trigger confidence

          IF humidity is high AND AQI is high:
              Increase combined trigger confidence

5. RANK TRIGGERS
   - Sort triggers based on confidence scores

6. SUGGEST SAFE ACTIONS
   IF AQI_trigger confidence is high:
       Suggest reducing outdoor exposure
       Suggest avoiding peak AQI hours

7. LEARN FROM OUTCOME
   - Observe symptoms over next few days
   - IF symptoms reduce:
         Increase confidence in trigger
     ELSE:
         Reduce confidence slightly



OUTPUTS:
- Ranked list of probable triggers
- Explanation of delayed AQI impact
- Risk trend summary (non-diagnostic)
