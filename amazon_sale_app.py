import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📈 Amazon Sale Report Dashboard")

df = pd.read_csv("Amazon Sale Report prateek.csv")

st.subheader("Raw Data")
st.dataframe(df)

if 'Category' in df.columns:
    categories = df['Category'].dropna().unique()
    selected_category = st.selectbox("Select Category", categories)
    df = df[df['Category'] == selected_category]

if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=False)

if 'Date' in df.columns and 'Amount' in df.columns:
    df_time = df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum().sort_index()
    df_time.index = df_time.index.to_timestamp()

    st.subheader("📊 Monthly Sales Trend")
    fig, ax = plt.subplots(figsize=(10, 5))
    df_time.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_ylabel("Total Amount (₹)")
    ax.set_xlabel("Month")
    st.pyplot(fig)

st.subheader("📌 Summary Statistics")
st.write(df.describe())
