import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from datetime import datetime

st.set_page_config(page_title="LA Wildfire Predictor", layout="wide")


@st.cache_data
def load_data():
    df = pd.read_csv("data/weather_enriched_with_emotion.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

@st.cache_resource
def load_model():
    return joblib.load("model/logistic_regression.pkl")

df = load_data()
model = load_model()


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard"])


if page == "Dashboard":
    st.title("LA Wildfire Dashboard")


    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Fire Occurrence Count")
        fire_counts = df["fire_occurred"].value_counts()
        fig1, ax1 = plt.subplots()
        ax1.pie(fire_counts, labels=["No Fire", "Fire"], autopct="%1.1f%%", startangle=90)
        ax1.axis("equal")
        st.pyplot(fig1)

    with col2:
        st.subheader("Temperature vs Fire")
        fig2, ax2 = plt.subplots()
        sns.boxplot(x="fire_occurred", y="temp_avg", data=df, ax=ax2)
        ax2.set_xticklabels(["No Fire", "Fire"])
        st.pyplot(fig2)


    st.subheader("Emotion Distribution")
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    sns.countplot(data=df, x="emotion", order=df["emotion"].value_counts().index, ax=ax3)
    plt.xticks(rotation=45)
    st.pyplot(fig3)


    st.subheader("Weather & Emotion Timeline (2014–2025)")
    df_sorted = df.sort_values("date")
    df_sorted["temp_avg_rolling"] = df_sorted["temp_avg"].rolling(30).mean()

    fig4 = go.Figure()


    fig4.add_trace(go.Scatter(x=df_sorted["date"], y=df_sorted["temp_avg"], name="Avg Temp (°C)", line=dict(color="blue")))
    fig4.add_trace(go.Scatter(x=df_sorted["date"], y=df_sorted["temp_max"], name="Max Temp", line=dict(color="orange", dash="dot")))
    fig4.add_trace(go.Scatter(x=df_sorted["date"], y=df_sorted["temp_min"], name="Min Temp", line=dict(color="green", dash="dot")))
    fig4.add_trace(go.Scatter(x=df_sorted["date"], y=df_sorted["temp_avg_rolling"], name="30-Day Avg", line=dict(color="black", dash="dash")))


    fig4.add_trace(go.Scatter(
        x=df_sorted["date"],
        y=df_sorted["emotion_score"],
        name="Emotion Score",
        line=dict(color="purple", width=1),
        yaxis="y2"
    ))

    fig4.add_trace(go.Scatter(
        x=[None], y=[None],
        mode='lines',
        line=dict(color='red', dash='dot'),
        name='Fire Event'
    ))


    for fire_date in df_sorted[df_sorted["fire_occurred"] == 1]["date"]:
        fire_date_py = fire_date.to_pydatetime()
        fig4.add_vline(x=fire_date, line=dict(color="red", width=1, dash="dot"))


    fig4.update_layout(
        title="Weather + Emotion + Fire Timeline",
        xaxis_title="Date",
        yaxis=dict(title="Temperature (°C)"),
        yaxis2=dict(title="Emotion Score", overlaying="y", side="right"),
        height=600,
        legend=dict(x=0.01, y=0.99),
        template="plotly_white"
    )

    st.plotly_chart(fig4, use_container_width=True)


    st.subheader("Dominant Emotion Trend Over Time")
    emotion_counts = df.groupby(["date", "emotion"]).size().unstack().fillna(0)
    fig5, ax5 = plt.subplots(figsize=(12, 5))
    emotion_counts.rolling(30).mean().plot(ax=ax5)
    ax5.set_ylabel("Frequency")
    ax5.set_xlabel("Date")
    ax5.set_title("Dominant Emotion (30-day Rolling Avg)")
    st.pyplot(fig5)
