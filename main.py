#import library
import streamlit as st
from web_function import load_data

from Tabs import home, predict, visualise

Tabs = {
    "Home" : home,
    "Prediction" : predict,
    "Visualisation" : visualise
}

#Membuat Sidebar
st.sidebar.title("Navigasi")

#Mmebuat Radio Opsi
page = st.sidebar.radio("Pages", list(Tabs.keys()))

#Load Dataset
df, x, y = load_data()

#Kondisi Call App Function
if page in["Prediction", "Visualisation"]:
    Tabs[page].app(df,x,y)
else:
    Tabs[page].app()