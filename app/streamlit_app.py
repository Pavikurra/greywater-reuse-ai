import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from generate_data import generate_water_data
from simulate_tank import simulate_tank

st.title("Greywater Reuse AI")

st.write(
    "AI-based greywater reuse simulation and sustainability analytics "
    "for apartment-scale water infrastructure."
)

st.sidebar.header("Simulation Settings")

apartments = st.sidebar.slider("Number of apartments", 10, 200, 50)
tank_capacity = st.sidebar.slider("Tank capacity in liters", 1000, 50000, 10000)

df = generate_water_data(apartments=apartments)
results = simulate_tank(df, tank_capacity_liters=tank_capacity)

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Greywater Generated",
    f"{results['incoming_greywater'].sum():,.0f} L"
)

col2.metric(
    "Freshwater Saved",
    f"{results['freshwater_saved'].sum():,.0f} L"
)

col3.metric(
    "Overflow",
    f"{results['overflow'].sum():,.0f} L"
)

st.subheader("Tank Level Over Time")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(results["date"], results["tank_level"])
ax.set_xlabel("Date")
ax.set_ylabel("Tank Level (Liters)")
ax.set_title("Greywater Tank Level Simulation")

st.pyplot(fig)

st.subheader("Simulation Data")

st.dataframe(results.head(20))
