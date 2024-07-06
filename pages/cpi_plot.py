import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the app
st.title("Interactive Graph from CSV")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the dataframe
    st.write("DataFrame:", df)

    # Select columns for x and y axes
    x_axis = st.selectbox("Select X-Axis Column", options=df.columns)
    y_axis = st.selectbox("Select Y-Axis Column", options=df.columns)

    # Create a plotly figure
    fig = px.scatter(df, x=x_axis, y=y_axis)

    # Display the figure
    st.plotly_chart(fig)
