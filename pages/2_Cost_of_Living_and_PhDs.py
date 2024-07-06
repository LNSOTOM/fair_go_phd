#import streamlit as st
#import pandas as pd
#import plotly.express as px

# Title of the app
#st.title("How has Cost of Living affected PhD students?")

# Read the CSV file
#df = pd.read_csv("assets/AllGroupsCPI.csv")

# Convert 'col_1' to datetime format
#df['col_1'] = pd.to_datetime(df['col_1'], format='%b-%y')

# Set 'col_1' as the index
#df.set_index('col_1', inplace=True)

# Plotting the data
#fig, ax = plt.subplots(figsize=(10, 6))
#ax.plot(df.index, df['col_2'], marker='o', label='Quarterly Change (%)')
#ax.plot(df.index, df['col_3'], marker='o', label='Annual Change (%)')
#ax.set_xlabel('Date')
#ax.set_ylabel('Percentage Change')
#ax.set_title('All groups CPI, Australia, quarterly and annual movement (%)')
#ax.legend()
#ax.grid(True)
#plt.xticks(rotation=45)
#plt.tight_layout()

# Display the plot in the Streamlit app
#st.pyplot(fig)
