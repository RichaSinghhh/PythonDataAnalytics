# Terminal -> cd Dashboard -> Enter
# streamlit run Home.py -> Enter
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as ps
import plotly.graph_objects as go

st.title("Titanic Data Analysis")

# Load the dataset
df = sns.load_dataset("titanic")

# Display the dataset
st.dataframe(df)