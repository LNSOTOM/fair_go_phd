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

infog1 = "assets/1.png"
st.image(infog1, use_column_width=True)

st.header("Who are PhD students?")

st.markdown(
"""
A PhD is the highest obtainable degree in a given discipline, and it results from a high-quality contribution to the field.  
Approximately ~50,000 PhD students are active within Australia; the majority work full-time on their project, which has a duration of 3.5 years.  
Once they graduate, PhD students may go on to stay within academia, or work in industry.  
"""
)

st.header("What do PhD students do?")

st.markdown(
"""
PhD students work on ground breaking, state of the art, frontline research with the guidance of a team of experts - this dynamic is similar to a graduate program, where a new employee is guided by senior figures to become fully qualified.  
PhD students work 40 hours a week and receive allocated time off (similarly to fully salaried staff members).  
PhD students have a very different workload and schedule compared to undergraduate or master students: they are expected to invest most of their working hours into their independent project, and do not attend classes or have time off during traditional school breaks.
"""
)

st.header("PhD students are a core driving force in research and innovation.")

st.markdown(
"""
PhD students make up over 50% of human resources dedicated to research in Australian universities. Their effort is key in keeping Australian research relevant and competitive.
"""
)

infog2 = "assets/2.png"
st.image(infog2, use_column_width=True)

st.header("How does this happen?")

st.markdown(
"""
PhD researchers receive a higher degree by research (HDR) stipend under the research training program (RTP) by the national government. As of 2024, the minimum full-time stipend is AUD 32,192.  
The 2024 PhD Stipend survey found that, even with top ups, most PhD researchers earn significantly less than the National Minimum Wage (AUD 47,627). Additionally, part-time PhD stipends are taxed.

Not only do PhD students not receive the equivalent of minimum wages, they also miss out on superannuation for several years.  
Universities can (and do) limit the amount of hours PhD researchers are allowed to take on outside work during business hours, limiting opportunities for extra income.
"""
)

#st.header("Where are we")

#m = leafmap.Map(center=[-25.2744, 133.7751], zoom=4, minimap_control=True)
# m.add_basemap("OpenTopoMap")
#m.add_tile_layer(
 #   url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
  #  name="Google Satellite",
   # attribution="Google",
#)
#m.to_streamlit(height=500)
