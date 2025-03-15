import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.info('This app will predict your obesity level!')

with st.expander('**Data**'):
  st.write('This is a raw data')
  df = pd.read_csv('https://raw.githubusercontent.com/JeffreyJuinior/dp-machinelearning/refs/heads/master/ObesityDataSet_raw_and_data_sinthetic.csv')
  df
  st.write('**X**')
  X = df.drop('HeartDisease',axis=1)
  X
  st.write('**y**')
  y = df['HeartDisease']
  y

with st.expander('**Data Visualization**'):
  st.scatter_chart(data=df, x = 'Cholesterol', y = 'RestingBP', color='HeartDisease')
