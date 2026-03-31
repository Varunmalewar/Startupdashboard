import streamlit as st 
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from pathlib import Path
st.set_page_config(layout="wide", page_title = 'Startup Dashboard')

base_dir = Path(__file__).resolve().parent
csv_candidates = [
    base_dir / 'start_up_cleaned (2).csv',
    base_dir / 'start_up_cleaned.csv',
    base_dir / 'startup_funding.csv',
]

csv_path = next((path for path in csv_candidates if path.exists()), None)
if csv_path is None:
    expected_files = ', '.join(path.name for path in csv_candidates)
    st.error(f'CSV file not found. Expected one of: {expected_files}')
    st.stop()

df = pd.read_csv(csv_path)
# Convert all columns to string to avoid Arrow serialization issues
# df = df.astype(str)
df['vertical'] = df['vertical'].astype(str)
df['date'] = pd.to_datetime(df['date'],errors = 'coerce')
df['monthly'] = df['date'].dt.month
df['year'] =df['date'].dt.year
# st.dataframe(df)


def load_overall_analysis():
    st.title('Overall Analysis')

    # total invested amount 
    total = round(df['amount'].sum())
    

    #maximum amount infused in startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending = False).head(1).values[0]
    

    #avg funding amount 
    avg_funding = df.groupby('startup')['amount'].sum().mean()
    

    # total funded startups
    num_startups = df['startup'].nunique()
    


    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric('Total',str(total)+' Cr') 
    with col2:
        st.metric('Max Funding',str(max_funding)+' Cr')
    with col3:
        st.metric('Avg Funding',str(round(avg_funding,2))+' Cr')
    with col4:
        st.metric('Total Funded Startups',num_startups)


    st.header("MOM Graph")
    selected_option = st.selectbox('Select Type',['Total','Count'])

    if selected_option == 'Total':
        temp_df = df.groupby(['year','month'])['amount'].sum().reset_index()
    
    else:
        temp_df = df.groupby(['year','month'])['amount'].count().reset_index()


    temp_df['x-axis']=temp_df['month'].astype(str) + '-' + temp_df['year'].astype(str) 
    temp_df[['amount','x-axis']]

    fig7, ax7 = plt.subplots()
    ax7.plot(temp_df['x-axis'],temp_df['amount'])
    st.pyplot(fig7)






def load_investor_details(investor):
    st.title(investor)

    # 5 investments done
    last_5_df = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]

    st.subheader("Most Recent Investments")
    st.dataframe(last_5_df)

    #biggest investment


    col1 , col2, col3 = st.columns(3)
    with col1:
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending = False).head(5)
        st.subheader("Biggest Investments")
        st.dataframe(big_series)

    
    with col2:
        st.subheader("Biggest Investments Visualization")
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)
    
    with col3 :
        st.subheader("Sectors invested in ")
        vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series,labels =vertical_series.index, autopct='%0.01f%%', startangle=140)
        st.pyplot(fig1)

    col4, col5 = st.columns(2)

    with col4:
        st.subheader('Investment Type')
        inv_type = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
        fig1, ax1 = plt.subplots()
        ax1.pie(inv_type,labels =inv_type.index, autopct='%0.01f%%', startangle=140)
        st.pyplot(fig1)

    with col5:
        st.subheader('City invested in')
        city = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
        fig1, ax1 = plt.subplots()
        ax1.pie(city,labels = city.index, autopct='%0.01f%%', startangle=140)
        st.pyplot(fig1)

    # print(df.info())
   
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()

    st.subheader("Year wise Investment")
    fig, ax = plt.subplots()
    ax.plot(year_series.index, year_series.values)
    st.pyplot(fig)









    





# # data cleaning 
# df['Investors Name']= df['Investors Name'].fillna('undisclosed')

st.sidebar.title("Startup funding analysis")
option = st.sidebar.selectbox("Select one",['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':

        load_overall_analysis()


elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Search Startup')
    st.title('Startup Analysis')

else:
    selected_investor = st.sidebar.selectbox('Select Investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Search Investor')

    if btn2:
        load_investor_details(selected_investor)


   


