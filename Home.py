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
#st.title("Fair Go for PhDs")

infog1 = "assets/fairgo_1.png"
st.image(infog1, use_column_width=True)

st.header("Who are PhD students?")

st.markdown(
"""
1. A PhD is the highest obtainable degree in a given discipline, and it results from a high-quality contribution to the field.  
2. Approximately ~50,000 PhD students are active within Australia; the majority work full-time on their project, which has a duration of 3.5 years.  
3. Once they graduate, PhD students may go on to stay within academia, or work in industry.  
"""
)

st.header("What do PhD students do?")

markdown = """
    1. PhD students work on ground breaking, state of the art, frontline research under the supervision of a team of experts.\\
    2. PhD students work 40 hours a week and receive allocated time off (similarly to staff members).\\
"""

st.markdown(markdown)

#st.header("Where are we")

#m = leafmap.Map(center=[-25.2744, 133.7751], zoom=4, minimap_control=True)
# m.add_basemap("OpenTopoMap")
#m.add_tile_layer(
 #   url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
  #  name="Google Satellite",
   # attribution="Google",
#)
#m.to_streamlit(height=500)
