import streamlit as st

st.write("# Visualisation using Streamlit")
st.write(
    """
    This is the main page of the application.
    
    The data used to be loaded from a CSV file and stored in the session state from this main page. This allowed it to be accessed from any page in the application.
    
    However, if you refreshed any page, the session state would be cleared and you would have to load the data from here again.
    
    This is extremely inconvenient so I instead just used the `@st.cache_data` decorator to cache the result of the `load_data` function.
    I did that originally as well but now I just import that function in all the pages that need it.
    I wasn't sure if importing things into the pages would work because of namespacing, and Python imports can get a little wonky like that.
    """
)
