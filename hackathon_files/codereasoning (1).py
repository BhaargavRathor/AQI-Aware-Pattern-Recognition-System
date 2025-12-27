
symptom_history = []     # Stores symptom severity per day (0–3)
aqi_history = []         # Stores AQI per day

trigger_confidence = {
    "AQI": 0.5           # Initial neutral confidence
}

SAFE_AQI_THRESHOLD = 150   # AQI above this is considered unhealthy


# -----------------------------
# Agent Observation
# -----------------------------

def observe(symptom_severity, aqi_value):
    """
    Store daily observations
    """
    symptom_history.append(symptom_severity)
    aqi_history.append(aqi_value)


# -----------------------------
# Flare Detection
# -----------------------------

def detect_flare():
    """
    Detect increase in respiratory symptom severity
    """
    if len(symptom_history) < 2:
        return False

    return symptom_history[-1] > symptom_history[-2]


# -----------------------------
# Delay-aware AQI Analysis
# -----------------------------

def analyze_aqi_delay():
    """
    Analyze AQI impact over delay windows (1–5 days)
    Returns a dictionary of delay_window : average_AQI
    """
    delays = {}

    for days in range(1, 6):
        if len(aqi_history) >= days:
            recent_aqi = aqi_history[-days:]
            delays[days] = sum(recent_aqi) / days

    return delays


# -----------------------------
# Confidence Update Logic
# -----------------------------

def update_confidence(aqi_delays):
    """
    Update AQI trigger confidence based on delay analysis
    """
    if not aqi_delays:
        return

    high_aqi_windows = 0

    for avg_aqi in aqi_delays.values():
        if avg_aqi > SAFE_AQI_THRESHOLD:
            high_aqi_windows += 1

    # Respiratory-specific logic:
    # multiple delayed high-AQI windows strengthen confidence
    if high_aqi_windows >= 2:
        trigger_confidence["AQI"] += 0.05
    else:
        trigger_confidence["AQI"] -= 0.03

    # Keep confidence between 0 and 1
    trigger_confidence["AQI"] = max(0, min(1, trigger_confidence["AQI"]))


# -----------------------------
# Explainable Reasoning Output
# -----------------------------

def explain_reasoning(aqi_delays):
    """
    Print agent reasoning in clear, human-readable form
    """
    print("\n--- Agent Explanation ---")
    print("AQI impact analysis across delay windows:")

    for days, avg in aqi_delays.items():
        print(f"  Past {days} day(s) average AQI: {avg:.1f}")

    confidence = trigger_confidence["AQI"]
    print(f"\nAQI trigger confidence score: {confidence:.2f}")

    if confidence > 0.7:
        print("High likelihood that poor air quality is contributing to respiratory symptoms.")
    elif confidence > 0.4:
        print("Moderate likelihood of AQI-related respiratory impact.")
    else:
        print("Low likelihood of AQI being a dominant respiratory trigger.")

    print("--------------------------")


# -----------------------------
# Example Simulation (Demo)
# -----------------------------

# Simulated daily data:
# (symptom_severity, AQI)
# symptom_severity: 0=None, 1=Mild, 2=Moderate, 3=Severe

daily_data = [
    (1, 120),  # Mild symptoms, moderate AQI
    (1, 135),
    (2, 160),  # AQI increases
    (3, 190),  # Symptom flare
    (3, 210),
]

print("Running Symptom Detective Agent Simulation...\n")

for symptom, aqi in daily_data:
    observe(symptom, aqi)

    if detect_flare():
        aqi_delays = analyze_aqi_delay()
        update_confidence(aqi_delays)
        explain_reasoning(aqi_delays)
