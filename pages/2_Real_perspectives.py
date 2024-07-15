import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
from PIL import Image


im = Image.open("assets/fairgo_logo.ico")
st.set_page_config(
    page_title="Fair Go for PhDs",
    page_icon=im,
    layout="wide",
)

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
- B, a PhD on Fisheries Management
"""
)
st.markdown("""---""")

st.markdown(
"""
"The tiny stipend combined with Hobart’s horrendous rental market meant that I got stuck in a pretty awful housing situation. My landlord didn’t care that the power went out all the time (almost daily), we had no heat, and limited hot water. My housemates and I had a pretty toxic falling out and they were actively trashing the place, so I was pretty sure that if I managed to move out I wouldn’t be getting any bond back. I spent so many nights in the PhD office because it had both light and heat, which my house often wouldn’t have. If I could have saved for a new bond + first month’s rent I would have, but even being as frugal as I could it was impossible. I stuck it out as long as I could before escaping and spending the last month of my candidature on a friend’s parent’s couch."
- a PhD from UTAS
"""
)
st.markdown("""---""")

st.markdown(
"""
"Living on a PhD scholarship presents daunting financial challenges. With 68% of my scholarship going towards rent ($480 per week), I rely on student loans to bridge the gap. Essential needs like housing, food, and healthcare require meticulous budgeting. Finding affordable housing near campus is crucial but expensive, exacerbated by health factors and lack of direct bill options for healthcare services, including eye and dental care. These costs and medications total approximately $6,500 annually, often exceeding what student health plans cover. Everyday expenses such as transportation, utilities, and academic supplies further strain my budget. The condensed three-year program leaves little room for leisure or travel, increasing the risk of burnout and emotional stress. This financial strain impacts not just immediate needs but also long-term planning and quality of life, highlighting the challenge of managing additional expenses like school supplies, telecommunications, clothing, grooming products, and miscellaneous items essential to daily living."
- a PhD from the University of Queensland
"""
)
st.markdown("""---""")
