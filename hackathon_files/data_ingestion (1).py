import pandas as pd
import random
from datetime import datetime, timedelta

def generate_sample_data(days=14):
    data = []
    start_date = datetime.today() - timedelta(days=days)

    for i in range(days):
        date = start_date + timedelta(days=i)

        data.append({
            "date": date.strftime("%Y-%m-%d"),
            "aqi": random.randint(50, 250),
            "pm25": round(random.uniform(10, 150), 2),
            
            "temperature": round(random.uniform(20, 38), 1),
            "humidity": round(random.uniform(30, 80), 1),
            "location": "Hyderabad"
        })

    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_sample_data()
    df.to_csv("sample_data.csv", index=False)
    print("Sample AQI + weather data generated successfully.")
