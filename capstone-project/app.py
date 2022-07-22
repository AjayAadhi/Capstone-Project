import streamlit
from predict_page import show_prediction_page
from explore_page import show_explore_page
import streamlit as st

val=st.sidebar.selectbox('Explore or Predict',('Predict','Explore'))

if(val == 'Predict'):
    show_prediction_page()

else:
    show_explore_page()
page_bg_img = """
<style>
.stApp {
background-image: url("https://www.theasset.com/storage/Image/2022/Jun/1654058996globecc.jpg");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
