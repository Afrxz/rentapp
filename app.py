import streamlit as st
from predictpage import show_predict_page
from explore_page import show_explore_page

a=st.sidebar.selectbox("Explore or predict",("Predict","Explore"))
if a == "Predict":
    show_predict_page()
elif a=="Explore":
    show_explore_page()


