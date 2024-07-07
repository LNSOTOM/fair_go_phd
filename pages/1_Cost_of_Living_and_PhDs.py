import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("How has Cost of Living affected PhD students?")

st.markdown(
"""
In the past few years, Cost of Living has increased significantly. Meanwhile, PhD stipends have been hovering around the Poverty Line, a metric that is calculated by the Melbourne Institute.
Poverty lines vary depending on income units; for example, the poverty line for a single person household is different than that for a couple, or families with dependents.  
As of 2024, the poverty line for a single person is AUD611.27; PhD students earn ~AUD619.08 per week on the minimum stipend rate.
"""
)
### PLOT HDR STIPEND VS. POVERTY LINE ###

# Read the CSV file
df = pd.read_csv("assets/hdr_rates.csv")

# Calculate the difference between stipend and poverty line
df['difference'] = df['weekly_full-time_base_rate_AUD'] - df['weekly_poverty_thresh_AUD']

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size

# Plot stipend and poverty line
ax.plot(df['Year'], df['weekly_full-time_base_rate_AUD'], marker='o', linestyle='-', color='blue', label='Minimum HDR stipend')  # Plot minimum HDR stipend
ax.plot(df['Year'], df['weekly_poverty_thresh_AUD'], marker='s', linestyle='--', color='orange', label='Poverty line')  # Plot poverty line

# Plot difference as a connecting line with labels
for index, row in df.iterrows():
    if row['difference'] >= 0:
        label = f"+${row['difference']:,.2f}"
    else:
        label = f"-${abs(row['difference']):,.2f}"
    
    ax.annotate(label, (row['Year'], row['weekly_full-time_base_rate_AUD']), xytext=(10,-10), textcoords='offset points', ha='center', fontsize=8, color='blue')

# Set labels and title
ax.set_xlabel('Year')  # x-axis label
ax.set_ylabel('Weekly HDR stipend rate (AUD)')  # y-axis label
plt.title('Minimum HDR Stipend vs Poverty Line')

# Add legend
ax.legend()

# Display plot in Streamlit
st.pyplot(fig)

### END PLOT 1
