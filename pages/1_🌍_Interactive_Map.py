import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

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

# Add custom CSS to position the select box
st.markdown("""
    <style>
    .selectbox-container {
        position: absolute;
        top: 10px;
        right: 10px;
        z-index: 1000;
        background-color: white;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Create a container for the select box
st.markdown('<div class="selectbox-container">', unsafe_allow_html=True)

options = list(leafmap.basemaps.keys())
index = options.index("SATELLITE")

basemap = st.selectbox("Select a basemap:", options, index)

st.markdown('</div>', unsafe_allow_html=True)

m = leafmap.Map(
    center=[-25.2744, 133.7751],
    zoom=4,
    locate_control=True,
    latlon_control=True,
    draw_export=True,
    # minimap_control=True
)
m.add_basemap(basemap)
m.to_streamlit(height=700)

