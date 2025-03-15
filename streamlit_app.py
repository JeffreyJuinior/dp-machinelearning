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
  Age = st.slider('Age', min_value = 14, max_value = 61, value = 24)
  Height = st.slider('Height', min_value = 1.45, max_value = 1.98, value = 1.7)
  Weight = st.slider('Weight', min_value = 39, max_value = 173, value = 86)
  FCVC = st.slider('FCVC', min_value = 1, max_value = 3, value = 2)
  NCP = st.slider('NCP', min_value = 1, max_value = 4, value = 3)
  CH2O = st.slider('CH2O', min_value = 1, max_value = 3, value = 2)
  FAF = st.slider('FAF', min_value = 0, max_value = 3, value = 1)
  TUE = st.slider('TUE', min_value = 0, max_value = 2, value = 1)
  
  Gender = st.selectbox('Gender', ('Male', 'Female'))
  
  

if __name__ == "__main__":
  main()
