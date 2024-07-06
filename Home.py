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

# Customize page title
st.title("Fair Go for PhDs")

infog1 = "assets/Fair_go_infog_1.png"
st.image(infog1, use_column_width=True)

st.header("Who are PhD students")

st.markdown(
"""
1.(some stats/demographics of PhD students in Australia! - pull some stats from dept of education?)\\
2.~50,000 Phd students in australia\\
3.Future professors, industry professionals, etc. 
"""
)

st.header("What do PhD students do")

markdown = """
    1.Expected to work 40 hrs/week year round.\\
    2.Ground breaking, state of the art, frontline research 
"""

st.markdown(markdown)

st.header("Where are we")

m = leafmap.Map(center=[-25.2744, 133.7751], zoom=4, minimap_control=True)
# m.add_basemap("OpenTopoMap")
m.add_tile_layer(
    url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    name="Google Satellite",
    attribution="Google",
)
m.to_streamlit(height=500)
