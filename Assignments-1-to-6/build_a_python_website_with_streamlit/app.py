import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("My First Streamlit Website")

# Text input
name = st.text_input("Enter your name:")

# Greet button
if st.button("Greet Me"):
    if name:
        st.write(f"Hello, {name}! Welcome to Streamlit.")
    else:
        st.write("Please enter your name to get greeted.")

# Slider to select number of points
num = st.slider("Select number of data points:", 10, 100, 50)

# Generate some random data
data = pd.DataFrame({
    'x': np.arange(num),
    'y': np.random.randn(num).cumsum()
})

# Display the line chart
st.line_chart(data)