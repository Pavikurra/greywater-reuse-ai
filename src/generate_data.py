import pandas as pd
import numpy as np

np.random.seed(42)

def generate_water_data(days=365, apartments=50, avg_residents_per_unit=2.2):

    dates = pd.date_range(
        start="2025-01-01",
        periods=days,
        freq="D"
    )

    residents = int(apartments * avg_residents_per_unit)

    data = []

    for date in dates:

        is_weekend = date.weekday() >= 5

        laundry_factor = 1.4 if is_weekend else 1.0

        shower_liters = np.random.normal(
            45 * residents,
            6 * residents
        )

        sink_liters = np.random.normal(
            8 * residents,
            2 * residents
        )

        laundry_liters = np.random.normal(
            18 * residents * laundry_factor,
            5 * residents
        )

        toilet_demand_liters = np.random.normal(
            28 * residents,
            4 * residents
        )

        greywater_generated = (
            shower_liters
            + sink_liters
            + laundry_liters
        )

        data.append({
            "date": date,
            "apartments": apartments,
            "residents": residents,
            "is_weekend": int(is_weekend),
            "shower_liters": max(shower_liters, 0),
            "sink_liters": max(sink_liters, 0),
            "laundry_liters": max(laundry_liters, 0),
            "toilet_demand_liters": max(toilet_demand_liters, 0),
            "greywater_generated": max(greywater_generated, 0)
        })

    return pd.DataFrame(data)

if __name__ == "__main__":

    df = generate_water_data()

    print(df.head())

    df.to_csv(
        "synthetic_water_data.csv",
        index=False
    )

    print("Synthetic dataset created.")
