import streamlit as st 
import pandas as pd
import numpy as np
import time

st.title("Startup Dashboard")
st.header("Welcome to the Startup Dashboard")
st.subheader("Selmon Bhai ")
st.write('This is a normal text')

st.markdown(""" 
### Heading 
- Race 3 
- Tiger Zinda Hai
- Tiger 3
""")

st.code("""
def foo(input):
    return input **2
x = foo(2)
print(x)

""")

st.latex(r'x^2 + y^2 = z^2')

df = pd.DataFrame({
    'name':['Varun','Selmon','Rahul'],
    'age':[21,22,24],
    'package':[1200000,3000000,400000]

})

st.dataframe(df)



st.metric('Revenue','Rs 10L','3%')


st.json({
    'name':['Varun','Selmon','Rahul'],
    'age':[21,22,24],
    'package':[1200000,3000000,400000]

})


st.image('2.jpg', width=300)  # Height auto-adjusts to maintain aspect ratio

st.video('task.mp4')
# st.audio('audio_file.mp3')  # Uncomment when you have an audio file



st.sidebar.title('Side ka title')



col1 , col2 , col3= st.columns(3) # side by side la sakte hai 

with col1:
    st.image('2.jpg', width=300)  # Height auto-adjusts to maintain aspect ratio

with col2:
    st.video('task.mp4')

with col3:
    st.subheader('This is the third column')



st.error('Login Failed !!')
st.success('Login Success !!')
st.warning('Login Warning !!')
st.info('Login Info !!')



bar = st.progress(0)
# for i in range(101):
#     # time.sleep(0.1)
#     bar.progress(i)



name = st.text_input('Enter your name')
password = st.text_input('Enter your password', type='password')
number = st.number_input("Enter age ",min_value = 17, max_value = 100, value = 22)


st.date_input('Enter your date of birth')
st.time_input('Enter your time')





