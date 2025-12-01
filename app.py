import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crop Recommendation System", layout="wide")

# ---------------------------
# Load Data
# ---------------------------
@st.cache_data
def load_data():
    data = pd.read_csv("./crop_production.csv")
    data['Season'] = data['Season'].str.strip()
    data['Crop'] = data['Crop'].str.strip()
    data = data.dropna()
    data['yield'] = data['Production'] / (data['Area'] + 0.0001)
    return data

data = load_data()

st.title("🌾 Crop Recommendation System (India)")
st.markdown("Select **State → District → Season** to get top recommended crops.")

# ---------------------------
# Input Controls
# ---------------------------

# State Selector
states = sorted(data["State_Name"].unique())
state = st.selectbox("Select State", states)

# District Selector (Filtered by State)
districts = sorted(data[data["State_Name"] == state]["District_Name"].unique())
district = st.selectbox("Select District", districts)

# Season Selector
seasons = sorted(data["Season"].unique())
season = st.selectbox("Select Season", seasons)

# Top 10 or Full List
best_crops_choice = st.checkbox("Show only Top 10 crops", value=True)

# ---------------------------
# Crop Recommendation Logic
# ---------------------------
def recommend_top_crops(df, state, district, season, best_crops_choice):
    df['Production_by_Area'] = df['Production'] / (df['Area'] + 0.0000001)
    
    filtered = df[
        (df["State_Name"] == state) &
        (df["District_Name"] == district) &
        (df["Season"] == season)
    ]

    if filtered.empty:
        return pd.DataFrame({"Crop": [], "Production_by_Area": []})

    if best_crops_choice:
        result = (
            filtered.groupby("Crop")["Production_by_Area"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )
    else:
        result = (
            filtered.groupby("Crop")["Production_by_Area"]
            .mean()
            .sort_values(ascending=False)
        )

    return result.reset_index()

# ---------------------------
# Show Results
# ---------------------------

if st.button("🔍 Recommend Crops"):
    result = recommend_top_crops(data, state, district, season, best_crops_choice)

    if result.empty:
        st.error("No data available for the selected filters!")
    else:
        st.success("Results Generated Successfully!")
        
        st.subheader(f"Top Crops for **{district}, {state}** ({season})")
        st.dataframe(result)

        import plotly.express as px

        fig = px.bar(
            result,
            x="Production_by_Area",
            y="Crop",
            orientation="h",
            title="Top Crops by Productivity",
            labels={"Production_by_Area": "Production per Area"},
            color="Production_by_Area",
            color_continuous_scale="viridis"
        )

        fig.update_layout(
            template="plotly_white",
            title_font_size=22,
            xaxis_title_font_size=16,
            yaxis_title_font_size=16,
            height=600
        )

        st.plotly_chart(fig, use_container_width=True)

