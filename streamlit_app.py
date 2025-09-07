import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

st.title("💳 Real-Time Fraud Detection System")

df = pd.read_csv("data/transactions.csv")

st.subheader("📊 Transaction Data Sample")
st.dataframe(df.head())

fraud_rate = df['is_fraud'].mean() * 100
st.metric(label="Fraud Rate (%)", value=f"{fraud_rate:.2f}%")

st.subheader("📈 Fraud by Merchant")
st.bar_chart(df.groupby('merchant')['is_fraud'].mean())

st.success("Demo placeholder: In production, this app would connect to a live transaction stream.")
