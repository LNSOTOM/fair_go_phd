import streamlit as st
import leafmap.foliumap as leafmap


# Customize the sidebar
markdown = """
Fair Go for PhDs
<https://x.com/RaiseHDRStipend>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "assets/instagram _1.png"
st.sidebar.image(logo)


st.title("Interactive Map")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("SATELLITE")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


with col1:

    m = leafmap.Map(
        center=[-25.2744, 133.7751],
        zoom =5, 
        locate_control=True, 
        latlon_control=True, 
        draw_export=True, 
        minimap_control=True
    )
    m.add_basemap(basemap)
    m.to_streamlit(height=700)
