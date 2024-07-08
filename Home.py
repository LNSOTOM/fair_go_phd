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

st.header("Our goal: fair wages for Australia's PhDs.")

st.markdown(
"""
'Go Fair for PhDs' is a campaign led by PhDs, for PhDs at the University of Tasmania (UTAS). Our goal is to ensure the just compensation of PhDs nationwide: we want the Australian government to raise the minimum stipend to match the national minimum wage, so that PhDs can live with dignity, afford housing and essentials, and focus on their research.
"""
)

st.subheader("Who are PhDs?")

st.markdown(
"""
A PhD is the highest obtainable degree in a given discipline, and it results from a high-quality contribution to the field.  
Approximately ~50,000 PhDs are active within Australia; the majority work full-time on their project, which has a duration of 3.5 years.  
Once they graduate, PhDs may go on to stay within academia, or work in industry.  
"""
)

st.subheader("What do PhDs do?")

st.markdown(
"""
PhDs work on ground breaking, state of the art, frontline research with the guidance of a team of experts - this dynamic is similar to a graduate program, where a new employee is guided by senior figures to become fully qualified.  
PhDs work at least 38 hours a week (and often more) and receive allocated time off similarly to fully salaried staff members.  
PhDs have a very different workload and schedule compared to undergraduate or master students: they are expected to invest most of their working hours into their independent project, and do not attend classes or have time off during traditional school breaks.
"""
)

st.header("PhDs are a core driving force in research and innovation.")

st.markdown(
"""
PhDs make up over 50% of human resources dedicated to research in Australian universities. Their effort is key in keeping Australian research relevant and competitive.
"""
)

infog2 = "assets/2.png"
st.image(infog2, use_column_width=True)

st.subheader("Why is this happening?")

st.markdown(
"""
PhDs receive a Higher Degree by Research (HDR) stipend under the Research Training Program (RTP) by the national government. As of 2024, the minimum full-time stipend is AUD 32,192.  
The 2024 PhD Stipend survey found that, even with top ups, most PhDs earn significantly less than the National Minimum Wage (AUD 47,627). Additionally, part-time PhD stipends are taxed.  
Not only do PhDs not receive the equivalent of minimum wages, they also miss out on superannuation for several years.  
Universities can (and do) limit the amount of hours PhDs are allowed to take on outside work during business hours, reducing opportunities for extra income.
"""
)

infog_help = "assets/help.png"
st.image(infog_help, use_column_width=True)

st.markdown(
"""
There are different ways to help:
1. Sign the e-petition submitted to the House of Representatives [here](https://www.aph.gov.au/e-petitions/petition/EN6358)  
2. Share our campaign on social media and within your networks  
3. Join us to help with our activities. We need a nation-wide network of PhDs, researchers, and senior staff to make our collective voice heard!​  
4. Share your own PhD experience with local media or [with us](https://fair-go-phd.streamlit.app/Get_in_touch)
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
