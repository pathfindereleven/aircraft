import streamlit as st
import pandas as pd

df = pd.read_csv("stats.csv")

st.write(df)