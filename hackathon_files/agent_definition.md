Symptom Detective Agent (Respiratory + AQI)

 1. AGENT OBJECTIVE

Air quality degradation has become a persistent and worsening public health
challenge in India, particularly in urban and semi-urban regions such as
Delhi, NCR, Punjab, Haryana, Uttar Pradesh, and parts of central India.
Prolonged exposure to high Air Quality Index (AQI) levels has led to a
noticeable rise in respiratory issues including asthma flare-ups, allergic
rhinitis, chronic cough, breathlessness, and pollution-induced lung stress.

While air pollution data is widely available, individuals suffering from
chronic or recurring respiratory symptoms often struggle to understand how
daily AQI exposure, weather conditions, and personal activity patterns
collectively influence their symptoms over time. The effects are frequently
delayed, cumulative, and non-obvious, making manual tracking ineffective.

The objective of the Symptom Detective Agent is to act as an intelligent,
AQI-aware reasoning system that helps users make sense of these complex,
time-delayed relationships.

Specifically, the agent aims to:
- Identify patterns linking air quality trends to respiratory symptom flare-ups
- Reason over delayed effects (e.g., symptoms appearing 1–3 days after
  high AQI exposure)
- Distinguish persistent environmental triggers from random symptom variation
- Adapt its understanding based on user-specific responses to pollution
- Provide explainable, non-clinical insights that improve user awareness and
  self-management

The agent does not diagnose respiratory diseases or recommend medical
treatment. Instead, it supports preventive awareness by helping users
understand how worsening air quality conditions may be contributing to
their respiratory health challenges over time.


2. SCOPE OF THE OBJECTIVE
The agent operates in a non-clinical, educational, and preventive scope.

Included:
- Respiratory symptom tracking
- Environmental factor analysis (AQI, pollution levels)
- Temporal pattern recognition
- Risk awareness and explanations

Excluded:
- Disease diagnosis
- Medication recommendations
- Emergency or clinical decision-making



3. AGENT GOAL
Primary Goal:
- Reduce the frequency and severity of respiratory symptom flare-ups by
  identifying probable environmental triggers.

Secondary Goals:
- Explain delayed effects between AQI exposure and symptoms
- Adapt trigger confidence based on observed outcomes
- Help users make informed, safe lifestyle adjustments


 4. AGENT STATE
The agent maintains a long-term internal state that includes:

- Symptom history:
  - Date
  - Severity level (e.g., low / medium / high)

- Environmental history:
  - Air Quality Index (AQI)
  - PM2.5 / PM10 levels
  - Temperature
  - Humidity

- Trigger hypotheses:
  - Potential triggers (e.g., high AQI, high humidity)
  - Time delay associated with each trigger
  - Confidence score for each trigger

- User context:
  - Outdoor exposure (yes/no)
  - Physical activity level (low/moderate/high)


 5. CONSTRAINTS AND SAFETY RULES
- The agent must not label or diagnose any disease.
- All outputs must be framed as probabilities or trends, not conclusions.
- Recommendations must be safe, reversible, and non-medical.
- The agent must clearly state uncertainty when confidence is low.



 6. EXAMPLE AGENT REASONING
If respiratory symptoms increase on a given day,
the agent examines AQI levels from the previous 1–5 days.

If elevated AQI repeatedly precedes symptom flare-ups,
the agent increases confidence that AQI is a potential trigger.

If the pattern does not repeat, confidence is reduced over time.
