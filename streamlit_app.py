import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.info('This app will predict your obesity level!')

st.expander('Data'):
  st.write('This is a raw data')
  df = pd.read_csv('https://raw.githubusercontent.com/JeffreyJuinior/dp-machinelearning/refs/heads/master/heart.csv')
  df
