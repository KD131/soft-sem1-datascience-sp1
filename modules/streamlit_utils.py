import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    df = pd.read_csv('data/3_geolocation.csv', index_col=0)
    return df
