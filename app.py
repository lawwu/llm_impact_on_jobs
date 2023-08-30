import streamlit as st
import pandas as pd
import numpy as np
import json

st.title('LLM Impact on Jobs')
st.write('''
Used llama2-13b-chat to assess the impact of LLMs on jobs. The set of job titles is 
ONET's list of occupations, which has 1,016 unique titles.
''')

# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
# INPUT_DATA = 'data/list_onet_titles_llm_risk_all.json'

@st.cache_data
def load_data():
    with open('./data/list_onet_titles_llm_risk_all.json', 'r') as f:
        data = json.load(f)
    data_json = json.loads(data)
    return data_json

df_onet_titles = pd.read_excel("./data/db_27_3_excel/Occupation Data.xlsx")
list_onet_titles = list(df_onet_titles['Title'])
data = load_data()

# Create a dropdown select box
selected_title = st.selectbox("Choose a job title", list_onet_titles)
# get index of selected title
index = list_onet_titles.index(selected_title)
st.subheader(f'How will LLMs affect {selected_title}?')
st.write(data[index]['generation'])
