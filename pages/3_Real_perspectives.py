import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Customize the sidebar
markdown = """
Fair Go for PhDs
<https://x.com/RaiseHDRStipend>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "assets/instagram _1.png"
st.sidebar.image(logo)

# Title of the app
st.title("How has Cost of Living affected PhDs?")

st.markdown(
"""
In the past few years, Cost of Living has increased significantly. Meanwhile, PhD stipends have been hovering around the Poverty Line, a metric that is calculated by the Melbourne Institute.
Poverty lines vary depending on income units; for example, the poverty line for a single person household is different than that for a couple, or families with dependents.    

As of 2024, the poverty line for a single person is AUD 611.27; PhDs earn ~AUD 619.08 per week on the minimum stipend rate.
"""
)
