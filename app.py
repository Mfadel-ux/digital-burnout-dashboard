import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import joblib
import sys

st.title("Burnout Test")

st.write("Python:", sys.version)
st.write("Sklearn:", sklearn.__version__)
st.write("Pandas:", pd.__version__)
st.write("Numpy:", np.__version__)
st.write("Joblib:", joblib.__version__)

try:
    model = joblib.load("burnout_predictor.pkl")

    st.success("Model Loaded")
    st.write(type(model))

except Exception as e:

    st.error("Load Failed")
    st.exception(e)
