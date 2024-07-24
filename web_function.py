#import modul
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st

@st.cache_data
def load_data():
    #Load Dataset
    data = pd.read_csv('D:/Web_Prediksi Penyakit hati/data_cleanginjal (1).csv')
    x = data[["bp", "sg", "al", "su", "rbc", "pc", "pcc", "ba", "bgr", "bu", "sc", "sod", "pot", "hemo", "pcv", "wc", "rc", "htn", "dm", "cad", "appet", "pe", "ane"]]
    y = data[['classification']]
    return data, x, y

@st.cache_resource
def train_model(x, y):
    model = DecisionTreeClassifier(
        ccp_alpha=0.0, class_weight=None, criterion='entropy', max_depth=4,
        max_features=None, max_leaf_nodes=None, min_impurity_decrease=0.0,
        min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0,
        random_state=42, splitter='best'
    ) 
    
    model.fit(x, y)
    score = model.score(x, y)
    return model, score

def predict(x, y, features):
    model, score = train_model(x, y)
    prediction = model.predict(np.array(features).reshape(1, -1))
    return prediction, score