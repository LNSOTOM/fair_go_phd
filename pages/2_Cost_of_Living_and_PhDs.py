import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("How has Cost of Living affected PhD students?")

# Read the CSV file
df = pd.read_csv("assets/AllGroupsCPI.csv")

# Plotting
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
plt.plot(df['col_1'], df['col_3'], marker='o', linestyle='-')  # Replace col_1 and col_3 with your actual column names
plt.xlabel('Time')  # Replace with appropriate x-axis label
plt.ylabel('Y Value')  # Replace with appropriate y-axis label
plt.title('Plot Title')  # Replace with your desired plot title

# Display plot in Streamlit
st.pyplot()
