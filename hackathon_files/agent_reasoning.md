Agent Reasoning Framework

1. Overview of the Reasoning Process
The Symptom Detective Agent operates as a continuous reasoning system that
observes respiratory symptoms and environmental conditions, analyzes delayed
relationships, and adapts its understanding over time.

The agent does not make one-time predictions. Instead, it follows an
iterative observe–reason–adapt loop.


2. Inputs Observed by the Agent
On each day, the agent observes the following inputs:

- Respiratory symptom severity reported by the user
  (e.g., none / mild / moderate / severe)

- Environmental data:
  - Air Quality Index (AQI)
  - PM2.5 and PM10 levels
  - Temperature
  - Humidity

- Contextual information:
  - Outdoor exposure (yes/no)
  - Physical activity level


3. Core Reasoning Loop

Step 1: Observation
The agent records daily symptom severity and corresponding environmental
conditions.

Step 2: Temporal Alignment
When an increase in symptom severity is detected, the agent examines
environmental data from the previous 1 to 5 days to account for delayed
effects of air pollution on respiratory health.


Step 3: Hypothesis Generation
Based on repeated patterns, the agent generates hypotheses such as:

- High AQI leads to respiratory flare-ups after a 1–3 day delay
- High humidity combined with poor AQI worsens symptoms
- Outdoor exposure during high AQI increases symptom severity

Each hypothesis is associated with:
- A time delay window
- A confidence score

Step 4: Confidence Update
If a hypothesis consistently aligns with observed symptom flare-ups,
its confidence score is increased.

If the pattern does not repeat over time, the confidence score is gradually
reduced.

This allows the agent to adapt its understanding to individual users.

Step 5: Trigger Ranking
All active hypotheses are ranked based on their confidence scores.
The agent highlights the most likely environmental triggers contributing
to recent symptoms.

Step 6: Safe Action Suggestion
To validate hypotheses, the agent may suggest safe, non-clinical actions
such as:

- Reducing outdoor exposure on high AQI days
- Monitoring symptoms after avoiding peak pollution hours
- Tracking symptom response to environmental changes

These actions are optional and reversible.

Step 7: Learning from Outcomes
The agent observes whether symptom severity improves or worsens following
suggested actions and updates hypothesis confidence accordingly.

This completes one reasoning cycle.

4. Key Characteristics of Agentic Behavior
- Long-term memory of symptoms and AQI trends
- Reasoning over delayed and cumulative effects
- Autonomous hypothesis generation
- Adaptation based on observed outcomes
- Explainable decision-making


5. Example Reasoning Scenario
If a user experiences severe symptoms on Day 5,
and AQI levels were consistently high on Days 2–4,
the agent increases confidence in a delayed AQI trigger hypothesis.

If similar patterns repeat, AQI is ranked as a strong trigger.
If not, the hypothesis is weakened over time.
