import streamlit as st
import pandas as pd
import duckdb
from PIL import Image

df = pd.read_csv("stats.csv")



st.set_page_config(
    page_title = "Aircraft Querry",
)

st.title("Aircraft Querry")

with st.form("layer_func"):
    classs = st.selectbox(
    'Aircraft class',
    ('na', 'fighter', 'bomber', 'attack', 'multirole', 'command', ' trainers', 'tanker','transport'))

    wing = st.selectbox(
    'Aircraft wing',
    ('na', 'swept', 'straight', 'tapered', 'delta', 'variable', 'specialty'))
    
    wingm = st.selectbox(
    'Wing Mounting',
    ('na', 'high', 'low', 'mid'))

    enginet = st.selectbox(
    'Engine type',
    ('na','jet', 'propeller'))

    enginem = st.selectbox(
    'Engine mounting',
    ('na','under_wing', 'in_wing', 'over_wing', 'fuselage', 'on_nose', 'tail'))

    enginec = st.selectbox(
    'engine count',
    ('na','1', '2', '3', '4', '5', '6', '7', '8'))

    fuselage= st.selectbox(
    'fuselage',
    ('na','thick', 'rectangular', 'tubular', 'slender'))

    tailv = st.selectbox(
    'Vertical tail',
    ('na','1', '2', '3'))

    tailh = st.selectbox(
    'Horizontal tail',
    ('na','high', 'low', 'mid'))
    
    st.form_submit_button('New Layer')
 
#st.write(classs)
qls= 0
if classs != "na":
    qls =(f" classs = '{classs}'")
q_string = (f"SELECT * FROM df where{qls}")

if wing != "na":
    qls =(f" and wing = '{wing}'")
    q_string = q_string + qls

if wingm != "na":
     qls =(f" and wingm = '{wingm}'")
     q_string = q_string + qls

if enginet != "na":
     qls =(f" and enginet = '{enginet}'")
     q_string = q_string + qls

if enginec != "na":
     qls =(f" and enginec = '{enginec}'")
     q_string = q_string + qls

if enginem != "na":
     qls =(f" and enginem = '{enginem}'")
     q_string = q_string + qls

if fuselage != "na":
     qls =(f" and fuselage = '{fuselage}'")
     q_string = q_string + qls

if tailv != "na":
     qls =(f" and tailv = '{tailv}'")
     q_string = q_string + qls

if tailh != "na":
     qls =(f" and tailh = '{tailh}'")
     q_string = q_string + qls


st.write(q_string)

qdf =  duckdb.query(q_string).df()
st.write(qdf)
st.write(q_string)

for i in qdf['name']:
    image = Image.open(f'resources/{i}.jpg')
    st.image(image, caption=i)