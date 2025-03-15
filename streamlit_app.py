import streamlit as st
import joblib
import pandas as pd

model = joblib.load('trained_model.pkl')
loaded_encoder = joblib.load('encoder.pkl')
loeaded_scaler = joblib.load('scaler.pkl')

def main():
  st.title('Machine Learning App')
  
  st.info('This app will predict your obesity level!')
  
  # Raw Data
  with st.expander('**Data**'):
    st.write('This is a raw data')
    df = pd.read_csv('https://raw.githubusercontent.com/JeffreyJuinior/dp-machinelearning/refs/heads/master/ObesityDataSet_raw_and_data_sinthetic.csv')
    df
    st.write('**X**')
    X = df.drop('NObeyesdad',axis=1)
    X
    st.write('**y**')
    y = df['NObeyesdad']
    y
  
  # Visualization
  with st.expander('**Data Visualization**'):
    st.scatter_chart(data=df, x = 'Height', y = 'Weight', color='NObeyesdad')
  
  # Input Data

def __input__ == "__main__":
  main()
