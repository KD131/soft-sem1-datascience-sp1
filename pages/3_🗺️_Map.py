import pandas as pd
import pydeck as pdk
import streamlit as st

from modules.streamlit_utils import load_data

df = load_data()

st.header("Map")
st.write("Here we'll show the locations of the various companies that we've collected. " \
    "We will use both the st.map() function which generates a scatter plot as well as PyDeck for more advanced stuff.")

st.subheader("st.map()")
st.write("This is a simple scatter plot, but it's super easy to create. As long as the DataFrame has columns named 'lat'/'latitude' and 'lon'/'longitude', it will work.")
st.write("Internally it uses PyDeck, which we'll look at next.")
st.map(df)

st.subheader("PyDeck")
st.write("PyDeck is built on top of Deck.gl, which is a WebGL-powered framework for visual exploratory data analysis of large datasets. " \
    "This lets us plot visualisations on top of geographical maps.")

init_view = pdk.data_utils.compute_view(df[['longitude', 'latitude']], view_proportion=0.9)
data = pd.DataFrame(df[['longitude', 'latitude', 'employees']])
data.fillna(0, inplace=True)

st.pydeck_chart(pdk.Deck(
    initial_view_state=init_view,
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=data,
            get_position='[longitude, latitude]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            get_elevation='employees',
            pickable=True,
            extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=data,
            get_position='[longitude, latitude]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        )
    ])
)

st.write("You have no idea how annoyed I am that I can't get the height to correspond to the number of employees. " \
    "There's a property called `get_elevation` which is supposed to do that, but it doesn't work. " \
    "Instead it just bins the companies based on location and assigns height based on size of bin. " \
    "This results in all of them being flat except one giant tower in the middle of Copenhagen because two companies were close together.")