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
st.title("A doctor's appointment away")

st.markdown(
"""
"I work over 40 hours per week on my PhD. The only way I can afford to do this is because I have a partner that has a well paying full-time job. I genuinely don't know how I would be able to do my research without him. Even so, we have to budget pretty carefully.  All you need is to have one unexpected dentist visit come up, and your bank account is empty. We are well into our 30s and can't even think about having kids, there is no way we could afford that right now. And just to re-iterate, I am very lucky by comparison. It's heart-breaking witnessing colleagues debate whether they should buy groceries or heat their homes. Many of us had careers before we started this. I had a competitive salary above Minimum Wage." - B, PhD on Fisheries Management
"""
)
