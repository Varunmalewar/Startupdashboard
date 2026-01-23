import streamlit as st
import pandas as pd

email = st.text_input("Enter your email")
password = st.text_input("Enter your password", type="password")

btn = st.button('Login karo ')

gender = st.selectbox('Select gender',['Male','Female','Others'])

# if btn is clicked 
if btn:
    if email == 'varunmalewar@gmail.com' and password == '123456':
        st.success("Login successful")
        st.write(gender)
        st.balloons()

    else:
        st.error("Login failed")



file = st.file_uploader('Upload your file', type=['csv', 'xlsx', 'xls'])

if file is not None:
    try:
        # Get file extension
        file_extension = file.name.split('.')[-1].lower()
        
        if file_extension == 'csv':
            df = pd.read_csv(file, encoding='latin-1', on_bad_lines='skip', engine='python')
        elif file_extension in ['xlsx', 'xls']:
            df = pd.read_excel(file, engine='openpyxl')
        else:
            st.error("Unsupported file format")
            df = None
        
        if df is not None:
            st.success(f"File uploaded successfully! ({len(df)} rows)")
            st.dataframe(df)
    except Exception as e:
        st.error(f"Error reading file: {str(e)}")
        st.info("Please ensure your file is properly formatted and not corrupted")