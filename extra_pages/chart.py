#%%
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from PIL import Image

# Configure Streamlit app
im = Image.open("assets/fairgo_logo.ico")
st.set_page_config(
    page_title="Fair Go for PhDs",
    page_icon=im,
    layout="wide",
)

# Sidebar customization
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
st.markdown("---")

st.markdown(
    """
    "I work over 40 hours per week on my PhD. The only way I can afford to do this is because I have a partner that has a well-paying full-time job. I genuinely don't know how I would be able to do my research without him. Even so, we have to budget pretty carefully. All you need is to have one unexpected dentist visit come up, and your bank account is empty. We are well into our 30s and can't even think about having kids, there is no way we could afford that right now. And just to re-iterate, I am very lucky by comparison. It's heart-breaking witnessing colleagues debate whether they should buy groceries or heat their homes. Many of us had careers before we started this. I had a competitive salary above Minimum Wage."   
    - B, PhD on Fisheries Management
    """
)
st.markdown("---")

# Create the data as a pandas DataFrame
data = pd.DataFrame({
    "position": [
        "Anthony Albanese\n(Australian Prime Minister)",
        "Jeremy Rockliff\n(Tasmanian Premier)",
        "Median Tasmanian",
        "Rufus Black\n(University of Tasmania Vice Chancellor)"
    ],
    "salary": [587000, 301397, 50130, 1115000],
    "salary_label": ["$587k", "$301k", "$50k", "$1.1m"],
    "group": [2, 2, 2, 1]
})

# Plot function
def plot_salary_comparison(data):
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create the barplot
    bars = sns.barplot(
        y=data['group'].astype(str),
        x=data['salary'],
        hue=data['position'],
        dodge=False,
        palette=["#D0DCD8", "#B8CAC6", "#A1B9B4", "#8AA8A3"],
        ax=ax
    )
    
    # Customize axis labels
    ax.set_xlabel("Annual salary (AUD)", fontsize=12)
    ax.set_ylabel(None)
    ax.set_xlim(0, 1150000)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${int(x):,}"))
    
    # Add labels to bars
    for bar, label in zip(bars.patches, data["salary_label"]):
        width = bar.get_width()
        y_pos = bar.get_y() + bar.get_height() / 2
        ax.text(width, y_pos, label, ha="center", va="center", fontsize=8, alpha=0.7)
    
    # Adjust legend
    ax.legend(title=None, ncol=1, loc="upper left", bbox_to_anchor=(1, 1))
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    plt.tight_layout()
    return fig

# Display the plot in Streamlit
st.pyplot(plot_salary_comparison(data))

# %%
