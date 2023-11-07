import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

model = joblib.load(r'C:\Users\thasa\Downloads\model.pkl')

st.title('Credit Approval Prediction')

# Create columns to organize input widgets
col1, col2, col3 = st.columns(3)

with col1:
    FLAG_OWN_CAR = st.selectbox('Do you own a car?', ['NO', 'YES'])
    FLAG_OWN_REALTY = st.selectbox('Do you own real estate?', ['NO', 'YES'])
    CNT_CHILDREN = st.number_input('Number of Children', min_value=0)
    AMT_INCOME_TOTAL = st.number_input('Income Amount')
    DAYS_EMPLOYED = st.number_input('Days Employed', min_value=0)

with col2:
    NAME_INCOME_TYPE = st.selectbox('Income Type', ['Commercial associate', 'Pensioner', 'State servant', 'Student', 'Working'])
    NAME_EDUCATION_TYPE = st.selectbox('Education Type', ['Academic degree', 'Higher education', 'Incomplete higher', 'Lower secondary', 'Secondary / secondary special'])
    NAME_FAMILY_STATUS = st.selectbox('Family Status', ['Civil marriage', 'Married', 'Separated', 'Single / not married', 'Widow'])
    NAME_HOUSING_TYPE = st.selectbox('Housing Type', ['Co-op apartment', 'House / apartment', 'Municipal apartment', 'Office apartment', 'Rented apartment', 'With parents'])
    FLAG_WORK_PHONE = st.selectbox('Do you have a work phone?', ['NO', 'YES'])

with col3:
    OCCUPATION_TYPE = st.selectbox('Occupation Type', ['Accountants', 'Cleaning staff', 'Cooking staff', 'Core staff', 'Drivers', 'HR staff', 'High skill tech staff', 'IT staff', 'Laborers', 'Low-skill Laborers', 'Managers', 'Medicine staff', 'Private service staff', 'Realty agents', 'Sales staff', 'Secretaries', 'Security staff', 'Waiters/barmen staff', 'nan'])
    CNT_FAM_MEMBERS = st.number_input('Number of Family Members')
    MONTHS_BALANCE = st.number_input('Months Balance', min_value=0)

if st.button('Predict Loan Approval'):
    # Create a dictionary with user input data
    input_data = {
        'FLAG_OWN_CAR': 1 if FLAG_OWN_CAR == 'YES' else 0,
        'FLAG_OWN_REALTY': 1 if FLAG_OWN_REALTY == 'YES' else 0,
        'CNT_CHILDREN': CNT_CHILDREN,
        'AMT_INCOME_TOTAL': AMT_INCOME_TOTAL,
        'NAME_INCOME_TYPE': ['Commercial associate', 'Pensioner', 'State servant', 'Student', 'Working'].index(NAME_INCOME_TYPE),
        'NAME_EDUCATION_TYPE': ['Academic degree', 'Higher education', 'Incomplete higher', 'Lower secondary', 'Secondary / secondary special'].index(NAME_EDUCATION_TYPE),
        'NAME_FAMILY_STATUS': ['Civil marriage', 'Married', 'Separated', 'Single / not married', 'Widow'].index(NAME_FAMILY_STATUS),
        'NAME_HOUSING_TYPE': ['Co-op apartment', 'House / apartment', 'Municipal apartment', 'Office apartment', 'Rented apartment', 'With parents'].index(NAME_HOUSING_TYPE),
        'DAYS_EMPLOYED': DAYS_EMPLOYED,
        'FLAG_WORK_PHONE': 1 if FLAG_WORK_PHONE == 'YES' else 0,
        'OCCUPATION_TYPE': ['Accountants', 'Cleaning staff', 'Cooking staff', 'Core staff', 'Drivers', 'HR staff', 'High skill tech staff', 'IT staff', 'Laborers', 'Low-skill Laborers', 'Managers', 'Medicine staff', 'Private service staff', 'Realty agents', 'Sales staff', 'Secretaries', 'Security staff', 'Waiters/barmen staff', 'nan'].index(OCCUPATION_TYPE),
        'CNT_FAM_MEMBERS': CNT_FAM_MEMBERS,
        'MONTHS_BALANCE': MONTHS_BALANCE
    }

    # Standardize the input data
    scaler = StandardScaler()
    input_data = [list(input_data.values())]  # Convert to a list
    input_data = scaler.fit_transform(input_data)

    # Make the prediction
    prediction = model.predict(input_data)

    # Display the result
    if prediction == -1:
        st.write("Loan Status: Omitted")
    elif prediction == 0:
        st.write("Loan Status: Denied")
    elif prediction == 1:
        st.write("Loan Status: Approved")
