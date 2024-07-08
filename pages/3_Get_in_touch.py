import streamlit as st
from PIL import Image
import leafmap.foliumap as leafmap
from streamlit_folium import st_folium
import folium
from folium.plugins import MiniMap

# Set page configuration
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
st.markdown("Are you someone from a media platform? Or someone with a story to tell? Please send any enquiries to micah.landonlane@utas.edu.au")


###########    
# # Center coordinates for mainland Australia
# australia_center = [-25.2744, 133.7751]

# # Create columns for layout
# col1, col2 = st.columns([4, 1])

# # List of available basemaps
# options = list(leafmap.basemaps.keys())
# index = options.index("SATELLITE")

# with col2:
#     # Select a basemap
#     basemap = st.selectbox("Select a basemap:", options, index)

# with col1:
#     # Create the map centered on Australia using leafmap
#     m = leafmap.Map(
#         center=australia_center,
#         zoom=4,
#         locate_control=True,
#         latlon_control=True,
#         draw_export=True,
#         minimap_control=True,
#     )
#     m.add_basemap(basemap)
    
#     m.to_streamlit(height=700)

###
##another options# Center coordinates for mainland Australia
australia_center = [-25.2744, 133.7751]

# Coordinates for Tasmania
tasmania_center = [-42.0409, 146.8087]
# Define basemaps manually
basemaps = {
    "OpenStreetMap": {
        "url": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        "attr": "© OpenStreetMap contributors"
    },
    "Google Satellite": {
        "url": "https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
        "attr": "Google"
    },
    "OpenTopoMap": {
        "url": "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png",
        "attr": "© OpenTopoMap (CC-BY-SA)"
    },
    "ESRI Antarctica": {
        "url": "https://services.arcgisonline.com/ArcGIS/rest/services/Polar/Antarctic_Imagery/MapServer/tile/{z}/{y}/{x}",
        "attr": "ESRI"
    },
    "ESRI Arctic": {
        "url": "https://services.arcgisonline.com/ArcGIS/rest/services/Polar/Arctic_Imagery/MapServer/tile/{z}/{y}/{x}",
        "attr": "ESRI"
    }
}


# Create the map centered on Australia using folium
m = folium.Map(location=australia_center, zoom_start=4, tiles=None)

# Add the fixed basemap (OpenTopoMap)
folium.TileLayer(basemaps["OpenTopoMap"]["url"], attr=basemaps["OpenTopoMap"]["attr"], name="OpenTopoMap").add_to(m)
    
# Add ESRI Antarctica layer
folium.TileLayer(
    tiles=basemaps["ESRI Antarctica"]["url"],
    attr=basemaps["ESRI Antarctica"]["attr"],
    name="ESRI Antarctica"
).add_to(m)

# Add ESRI Arctic layer
folium.TileLayer(
    tiles=basemaps["ESRI Arctic"]["url"],
    attr=basemaps["ESRI Arctic"]["attr"],
    name="ESRI Arctic"
).add_to(m)

# Add Google Satellite layer
folium.TileLayer(
    tiles="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    attr="Google",
    name="Google Satellite",
).add_to(m)

# Add MiniMap centered on Tasmania
minimap = MiniMap(toggle_display=True, position="bottomleft")
minimap.add_to(m)

# Add a marker in Tasmania with a custom icon
icon = folium.Icon(icon="home", color="#FDD072", icon_color="blue")
folium.Marker(location=tasmania_center, popup="Tasmania", icon=icon).add_to(m)

# Add Layer control
folium.LayerControl().add_to(m)

# Custom JavaScript to set the minimap view to Tasmania
custom_js = f"""
<script>
    document.addEventListener("DOMContentLoaded", function() {{
        var minimap = document.querySelector('.leaflet-control-minimap');
        if (minimap) {{
            minimap._miniMap.setView([{tasmania_center[0]}, {tasmania_center[1]}], 5);
        }}
    }});
</script>
"""
folium.Element(custom_js).add_to(m.get_root())

# Display the map in Streamlit with a height of 700 pixels and a width of 800 pixels
st_folium(m, height=400,  width="100%")