import streamlit as st 
import pandas as pd
import numpy as np
import time

df = pd.read_excel(r'D:\Python\Pandas\Streamlit\shove.xlsx', engine='openpyxl')
# Convert all columns to string to avoid Arrow serialization issues
df = df.astype(str)
# st.dataframe(df)

# data cleaning 
df['Investors Name']= df['Investors Name'].fillna('undisclosed')

st.sidebar.title("Startup funding analysis")
option = st.sidebar.selectbox("Select one",['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')


elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['Startup Name'].unique().tolist()))
    btn1 = st.sidebar.button('Search Startup')
    st.title('Startup Analysis')

else:
    st.sidebar.selectbox('Select Investor',sorted(df['Investors Name'].unique().tolist()))
    btn2 = st.sidebar.button('Search Investor')
    st.title('Investor Analysis')


