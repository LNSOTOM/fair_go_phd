import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

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
st.title("Groceries, heating, or a doctor's appointment?")

st.markdown(
"""
As part of the campaign, we want to highlight the difficulties faced by current PhDs - a low stipend has ramifications that go beyond comfort, but affect people's physical and mental health. 
PhDs are already [vulnerable to anxiety and depression](https://www.nature.com/articles/s41599-021-00983-8) due to the high pressure environment of academia; low stipends aggravate this situation and stop PhDs from asking for doctor's appointments, or being able to live without having to choose between groceries, heating, or their own wellbeing.
"""
)
st.markdown("""---""")

st.markdown(
"""
"I work over 40 hours per week on my PhD. The only way I can afford to do this is because I have a partner that has a well paying full-time job. I genuinely don't know how I would be able to do my research without him. Even so, we have to budget pretty carefully.  All you need is to have one unexpected dentist visit come up, and your bank account is empty. We are well into our 30s and can't even think about having kids, there is no way we could afford that right now. And just to re-iterate, I am very lucky by comparison. It's heart-breaking witnessing colleagues debate whether they should buy groceries or heat their homes. Many of us had careers before we started this. I had a competitive salary above Minimum Wage."   
- B, PhD on Fisheries Management
"""
)
st.markdown("""---""")
