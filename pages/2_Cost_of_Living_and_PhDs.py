import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the app
st.title("How has Cost of Living affected PhD students?")

# Read the CSV file
    df = pd.read_csv("assets/AllGroupsCPI.csv")

    # Select columns for x and y axes
    x_axis = st.selectbox("Select X-Axis Column", options=df.columns)
    y_axis = st.selectbox("Select Y-Axis Column", options=df.columns)

    # Create a plotly figure
    fig = px.scatter(df, x=x_axis, y=y_axis)

    # Display the figure
    st.plotly_chart(fig)
