import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    df = pd.read_csv('data/3_geolocation.csv', index_col=0)
    return df

st.session_state.df = load_data()

# st.sidebar.divider()

st.write("# Visualisation using Streamlit")
st.markdown(
    """
    This is the main page of the application.
    
    The data is loaded from a CSV file and stored in the session state. This allows it to be accessed from any page in the application.
    
    However, if you refresh any page, the session state will be cleared and you will have to load the data from here again.
    
    This is extremely inconvenient so I might stop doing that.
    """
)

