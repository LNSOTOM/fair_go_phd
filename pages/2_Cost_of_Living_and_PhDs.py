import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("How has Cost of Living affected PhD students?")

# Read the CSV file
df = pd.read_csv("assets/hdr_rates.csv")

# Plotting up figure
fig = plt.figure(figsize=(10, 6))  # Adjust the figure size 
plt.plot(df['Year'], df['weekly_full-time_base_rate_AUD'], marker='o', linestyle='-', label='Minimum HDR stipend')  # Plot minimum HDR stipend
plt.plot(df['Year'], df['weekly_poverty_thresh_AUD'], marker='s', linestyle='--', color='orange', label='Poverty line')  # Plot poverty line

plt.xlabel('Year')  # x-axis label
plt.ylabel('Weekly HDR stipend rate (AUD)')  # y-axis label
plt.title('Minimum HDR Stipend vs Poverty Line')  # Plot title

# Display plot in Streamlit
st.pyplot(fig)

