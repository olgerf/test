import streamlit as st
from streamlit_folium import st_folium
import folium

map = folium.Map(location = [52.2129919, 5.2793703], zoom_start=7, tiles=None)
base_map = folium.FeatureGroup(name='Basemap', overlay=True, control=False)
folium.TileLayer(tiles='OpenStreetMap').add_to(base_map)
base_map.add_to(map)
st_data = st_folium(map)