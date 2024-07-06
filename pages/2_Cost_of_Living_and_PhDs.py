import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("How has Cost of Living affected PhD students?")

# Read the CSV file
df = pd.read_csv("assets/AllGroupsCPI.csv")


# Plotting
fig = plt.figure(figsize=(10, 6))  # Adjust the figure size 
plt.plot(df['col_1'], df['col_3'], marker='o', linestyle='-')
plt.xlabel('Time')  # x-axis label
plt.ylabel('CPI')  # y-axis label

# Display plot in Streamlit
st.pyplot()

