import streamlit as st
import pickle
import numpy as np
from warnings import filterwarnings
filterwarnings('ignore')

model = pickle.load(open('model.pkl', 'rb'))

st.title("Iris-Flower Classification")

sepal_length = st.number_input("Sepal Length: ")

sepal_width = st.number_input("Sepal Width: ")

petal_length = st.number_input("Petal Length: ")

petal_width = st.number_input("Petal Width: ")

if st.button('Predict'):
    # 1. predict
    result = str(model.predict(np.array([[sepal_length, sepal_width, petal_length, petal_width]])).tolist())
    result = result[2:-2]
    # 2. Display
    st.header(f"Type: {result}")

