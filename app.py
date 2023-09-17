# app.py

import streamlit as st
from visualization import generate_bar_chart

st.title('Simple Data Visualization App')

data = st.slider('Select data values', 1, 100, (10, 20, 30, 40))
labels = ['A', 'B', 'C', 'D']

generate_bar_chart(data, labels)

st.image('chart.png')
