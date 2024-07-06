import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("How has cost of living affected PhD students?")

# Read the CSV file
df = pd.read_csv("assets/hdr_rates.csv")

# Calculate the difference between stipend and poverty line
df['difference'] = df['weekly_full-time_base_rate_AUD'] - df['weekly_poverty_thresh_AUD']

# Plot stipend and poverty line
ax.plot(df['Year'], df['weekly_full-time_base_rate_AUD'], marker='o', linestyle='-', color='blue', label='Minimum HDR stipend')  # Plot minimum HDR stipend
ax.plot(df['Year'], df['weekly_poverty_thresh_AUD'], marker='s', linestyle='--', color='orange', label='Poverty line')  # Plot poverty line

# Plot difference as a connecting line with labels
for index, row in df.iterrows():
    label = f"${abs(row['difference']):,.2f}"
    ax.annotate(label, (row['Year'], row['weekly_full-time_base_rate_AUD']), textcoords="offset points", xytext=(0,10), ha='center', color='green')

# Set labels and title
ax.set_xlabel('Year')  # x-axis label
ax.set_ylabel('Weekly HDR stipend rate (AUD)')  # y-axis label
plt.title('Minimum HDR Stipend vs Poverty Line')

# Add legend
ax.legend()

# Display plot in Streamlit
st.pyplot(fig)

