import streamlit as st

st.write("## Table")
if not 'df' in st.session_state:
    # st.write("""Please go to <a target="_self" href="/">main page</a> to load data.""", unsafe_allow_html=True)
    st.warning("Please go to main page to load data.", icon='🔥')
    st.stop()

st.write("This table shows the data on the various companies that we've collected.")
st.session_state.df