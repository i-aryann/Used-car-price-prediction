import joblib
import streamlit as st
import numpy as np

pickle_model = open('./car_price_model.pkl', 'rb')
pickle_scaler= open('./model_scaler.pkl','rb')
pickle_encoder= open('./label_encoder.pkl','rb')
model_clf = joblib.load(pickle_model)
model_scaler=  joblib.load(pickle_scaler)
model_encoder= joblib.load(pickle_encoder)
