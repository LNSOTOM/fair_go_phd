import streamlit as st
import matplotlib.pyplot as plt

# Title of the app
st.title("How has Cost of Living affected PhD students?")

# Read the CSV file
df = pd.read_csv("assets/AllGroupsCPI.csv")

# Convert 'col_1' to datetime format
df['col_1'] = pd.to_datetime(df['col_1'], format='%b-%y')

#create your figure and get the figure object returned
fig = plt.figure() 
st.pyplot(fig)
