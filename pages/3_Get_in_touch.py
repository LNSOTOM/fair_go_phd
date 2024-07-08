import streamlit as st

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

st.title("Get in touch with us!")

st.markdown("Are you someone from a media platform? Or someone with a story to tell?")
