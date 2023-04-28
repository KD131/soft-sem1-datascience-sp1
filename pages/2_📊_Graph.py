import streamlit as st

from modules.streamlit_utils import load_data

df = load_data()

st.header("Graph")
"Let's plot a graph of the number of employees in each company."
"We'll do a simple bar chart with st.bar_chart(). Internally it uses Altair which you can also call explicitly to customise it more."

col1, col2, col3 = st.columns(3)
col1.metric(label="Number of companies*", value=df.shape[0])
col2.metric(label="Avg. number of employees", value=round(df['employees'].mean(), 2))
col3.metric(label="Median number of employees", value=round(df['employees'].median(), 2))

st.bar_chart(df['employees'])

f"*\* {df['employees'].isna().sum()} of those companies have no data on number of employees and aren't counted.*"
