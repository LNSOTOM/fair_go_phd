import streamlit as st
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

st.title("Get in touch with us!")

st.markdown("Are you someone from a media platform? Or someone with a story to tell?  Please send any enquiries to micah.landonlane@utas.edu.au")
