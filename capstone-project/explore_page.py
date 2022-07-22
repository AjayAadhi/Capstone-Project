import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import streamlit as st
from PIL import Image

def load_data():
    with open('saved_steps.pkl', 'rb') as file:
         data1 = pickle.load(file)
    return data1

data1 = load_data()
df = data1['data']
def show_explore_page():
     st.write("# Visualization ")
     Visualize1=st.button('Number Of Countries In Each Region')
     if Visualize1:
            # fig, ax = plt.subplots(figsize=(10,8))
            # ax = sns.countplot(x=df['Region'], order=df['Region'].value_counts(ascending=False).index);              
            # abs_values = df['Region'].value_counts(ascending=False)
            # rel_values = df['Region'].value_counts(ascending=False, normalize=True).values * 100
            # lbls = [f'{p[0]} ({p[1]:.0f}%)' for p in zip(abs_values, rel_values)]

            # ax.bar_label(container=ax.containers[0], labels=lbls)
            # plt.xticks(rotation=90)
            # plt.show()
            reg_count = Image.open("reg_count.jpg")
            st.image(reg_count)
            # , caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto'
     Visualize2=st.button('Population In Each Region')
     if Visualize2:
        population = Image.open("population.jpg")
        st.image(population)
     Visualize3=st.button('GDP ($ per capita)')
     if Visualize3:
        gdp = Image.open("gdp.jpg")
        st.image(gdp)
     Visualize4=st.button('Correlation With Each Attribute')
     if Visualize4:
        corr = Image.open("correlation.jpg")
        st.image(corr)  
     Visualize5=st.button('Factors Affectin The GDP')
     if Visualize5:
        factors = Image.open("factors.jpg")
        st.image(factors)        
     clear=st.button('Clear graph')     
     if clear:
            st.write(" ")