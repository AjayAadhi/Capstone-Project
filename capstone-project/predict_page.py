import streamlit as st
import pickle
import numpy as np
import sklearn 
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from PIL import Image



def load_model():
    with open('saved_steps.pkl', 'rb') as file:
         data1 = pickle.load(file)
    return data1

data1 = load_model()
rf = data1['model']

def callback():
         st.session_state.button_clicked =True


def show_prediction_page():
     st.title('Factors Affecting The GDP')
     gdp1 = Image.open("gdp_logo.jpg")
     st.image(gdp1, width=100)
     st.header(""" We need data of the country""")

     # uploaded_file = st.file_uploader("Upload your csv file", type=["csv"], accept_multiple_files=False)
     # df=pd.read_csv(uploaded_file)
     # ok=st.button("Display Data")
     # clear=st.button('Clear Data')
     # if ok:
     #       st.write(df)      
     # if clear:
     #       st.write(" ")
     
     
     # Predict=st.button('Predict GDP')
     # if Predict:
     #      var=rf.predict(df)
     #      st.write(var)       
     
   #   uploaded_files = st.file_uploader("Choose a CSV file", type=['png', 'jpg'])
     uploaded_file = st.file_uploader("Upload your csv file", type=["csv"], accept_multiple_files=False )
     col1, col2, col3 , col4 = st.columns(4)
   #   with col1:
   #      display=col1.button("Display Data")
   #   with col2:
   #      pass
   #   with col4:
   #      predict=col4.button("Predict")
   #   with col3 :
   #      pass
     if uploaded_file is not None:
        df=pd.read_csv(uploaded_file)
   #      if display:
   #          clear=st.button("Clear")  
   #          st.write(df)
   #          if clear:
   #              st.write("")
   #      if predict:        
   #          result=rf.predict(df)
   #          st.subheader(f"The Predicted GDP is $ {round(result[0],2)}")   
     # ans = rf.predict(df)
     # st.write(ans)
    ###"CREATING THE NESTED IF TO GET NESTED BUTTON"
     if "button_clicked" not in st.session_state:
         st.session_state.button_clicked = False
                 
     if(
         st.button('DISPLAY' , on_click=callback)
         or st.session_state.button_clicked
      ):
         st.write(df)
         if st.button('PREDICTION'):
             result=rf.predict(df)
             st.subheader(f"The Predicted GDP is $ {round(result[0],2)}")
               



 
 