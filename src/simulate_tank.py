import pandas as pd


def simulate_tank(df, tank_capacity_liters=10000, initial_tank_level=0):
    tank_level = initial_tank_level
    results = []

    for _, row in df.iterrows():
        incoming_greywater = row["greywater_generated"]
        reuse_demand = row["toilet_demand_liters"]

        tank_level += incoming_greywater

        overflow = max(tank_level - tank_capacity_liters, 0)

        if overflow > 0:
            tank_level = tank_capacity_liters

        reused_water = min(tank_level, reuse_demand)
        tank_level -= reused_water

        shortage = max(reuse_demand - reused_water, 0)

        results.append({
            "date": row["date"],
            "incoming_greywater": incoming_greywater,
            "reuse_demand": reuse_demand,
            "reused_water": reused_water,
            "tank_level": tank_level,
            "overflow": overflow,
            "shortage": shortage,
            "freshwater_saved": reused_water
        })

    return pd.DataFrame(results)


if __name__ == "__main__":
    df = pd.read_csv("synthetic_water_data.csv")
    results = simulate_tank(df)

    print(results.head())

    results.to_csv("tank_simulation_results.csv", index=False)

    print("Tank simulation completed.")
