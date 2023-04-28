import streamlit as st

from modules.streamlit_utils import load_data

# Session state way of fetching the DataFrame. Requires the data to be loaded from the main page.
# if not 'df' in st.session_state:
#     # st.write("""Please go to <a target="_self" href="/">main page</a> to load data.""", unsafe_allow_html=True)
#     st.warning("Please go to main page to load data.", icon='🔥')
#     # st.stop()
# df = st.session_state.df

df = load_data()

st.write("## Table")
st.write("This table shows the data on the various companies that we've collected.")
df