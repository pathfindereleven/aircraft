

import streamlit as st
with st.form("layer_func"):
    layer_name = st.text_input("layer Name", "Name")
    source = st.text_input("Source", "source")
    min = st.slider("Minimum", 0,22, 0)
    max = st.slider("Maximum", 0,22, 22)

    submitted = st.form_submit_button("Submit")
    if submitted: 
        dictionary["key"]  = {
            layer_name: {
            "source": source,
            "min": min,
            "max": max
            }
        }

if st.button('New Layer'):
    layer_func()