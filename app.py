import streamlit as st
import pandas as pd
import numpy as np
import json
import random

st.title('LLM Impact on Jobs')
st.write('''
Used llama2-13b-chat to assess the impact of LLMs on jobs. The set of job titles is 
ONET's list of occupations, which has 1,016 unique titles.
''')

@st.cache_data
def load_data():
    with open('./data/list_onet_titles_llm_risk_all.json', 'r') as f:
        data = json.load(f)
    data_json = json.loads(data)
    return data_json

# Load Data
df_onet_titles = pd.read_excel("./data/db_27_3_excel/Occupation Data.xlsx")
list_onet_titles = list(df_onet_titles['Title'])
data = load_data()

# Initialize or get state
if 'selected_title' not in st.session_state:
    st.session_state.selected_title = list_onet_titles[0]

# Create a button for random selection
if st.button('Select Random Job Title'):
    st.session_state.selected_title = random.choice(list_onet_titles)

# Create a dropdown select box and bind to session_state
st.session_state.selected_title = st.selectbox(
    "Or choose a job title manually",
    list_onet_titles,
    index=list_onet_titles.index(st.session_state.selected_title)
)

# Get index of selected title
index = list_onet_titles.index(st.session_state.selected_title)

# Display results
st.subheader(f'How will LLMs affect {st.session_state.selected_title}?')
st.write(data[index]['generation'])