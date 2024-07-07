import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("How has Cost of Living affected PhD students?")

st.markdown(
"""
In the past few years, Cost of Living has increased significantly. Meanwhile, PhD stipends have been hovering around the Poverty Line, a metric that is calculated by the Melbourne Institute.
Poverty lines vary depending on income units; for example, the poverty line for a single person household is different than that for a couple, or families with dependents.    

As of 2024, the poverty line for a single person is AUD 611.27; PhD students earn ~AUD 619.08 per week on the minimum stipend rate.
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

st.markdown(
"""
As a consequence, financial stress is an ever-present factor for most PhD students that cannot rely on savings, family support, or a partner. This greatly limits the pool of people that can afford to do a PhD, excluding talent, and reducing accessibility to postgraduate programs.  

Many PhD students are a medical emergency away from having to pause or drop out from their PhD program. How is underpaying its core workforce a sustainable option for research?
"""
)

# Create a DataFrame directly in the code
# Create a DataFrame directly in the code
budget_data = {
    "Budget Category": ["PhD stipend (annual)", "Rent in Hobart (sharehouse or small studio", "Single-person groceries", "Utilities and additional costs", "Cost of a cheap car (purchase and running costs)", "Annual remainder", "Weekly remainder"],
    "Expense": [32195, -12567, -4651, -6240, -4037, 4700, 90]
}

budget_df = pd.DataFrame(budget_data)

# Display the dataframe as a table
st.subheader("Budget and Expenses Table")
st.table(budget_df) 

