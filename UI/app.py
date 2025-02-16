import streamlit as st  
import numpy as np
import joblib
import warnings

warnings.filterwarnings('ignore')

st.header("Salary Prediction")  
st.subheader("Predicting Whether Salary is Greater or Less Than 50K")  

st.write(  
    """  
    This model predicts salary based on input features such as **age, workclass, education, education number, marital status, occupation, relationship, sex, capital gain, capital loss, and hours per week**.  

    The model is built using **Naïve Bayes** and achieves an **accuracy of 80%**.  
    """  
)  

st.subheader("Your Work Performance")  

# Creating two columns  
col1, col2 = st.columns(2)  

# Left Column  
with col1:  
    age = st.number_input("Enter your Age:", step=1, min_value=17, max_value=90)  

    workClassFeatureValues = ['Private Sector', 'Self-Employed', 'Government']  
    workClass = st.selectbox('Work Class:', workClassFeatureValues)  

    educationFeatureValues = ['Bachelor’s Degree', 'College', 'Doctorate', 'High School',
                              'High School Graduate', 'Master’s Degree', 'Middle School', 'No Education', 
                              'Primary', 'Professional Degree', 'Associate Degree']  
    education = st.selectbox("Education", educationFeatureValues)  

    educationNo = st.number_input("Education Number:", step=1, min_value=1, max_value=16)  

    maritalStatusFeatureValues = ["Married", "Married but Separated", "Separated", "Single", "Widowed", "Divorced"]    
    maritalStatus = st.selectbox("Marital Status", maritalStatusFeatureValues)  

    occupationFeatureValues = ['Clerical', 'Domestic Work', 'Labor', 'Management', 'Manufacturing', 
                               'Military', 'Professional', 'Sales', 'Security', 'Service', 
                               'Skilled Trades', 'Technical', 'Transportation', 'Agriculture']
    
    occupation = st.selectbox("Occupation", occupationFeatureValues)  

# Right Column  
with col2:  
    relationShipFeatureValues = ['Extended Family', 'Independent', 'Single', 'Spouse', 'Child']
    relationShip = st.selectbox("Relationship", relationShipFeatureValues)  

    sexFeatureValues = ['Male', 'Female']  
    sex = st.selectbox("Sex", sexFeatureValues)  

    capitalGain = st.number_input("Capital Gain:", step=1, min_value=0)  
    capitalLoss = st.number_input("Capital Loss:", step=1, min_value=0)  
    hourPerWeek = st.number_input("Hours per Week:", step=1, min_value=0)  


submit = st.button("Submit")

def one_hot_encode(value, categories):
    """One-hot encode a categorical variable with drop_first=True"""
    encoding = [1 if value == cat else 0 for cat in categories[:-1]]  # Drops last category
    return encoding

if submit:
    # Encoding categorical features
    workClass_encoded = one_hot_encode(workClass, workClassFeatureValues)
    education_encoded = one_hot_encode(education, educationFeatureValues)
    maritalStatus_encoded = one_hot_encode(maritalStatus, maritalStatusFeatureValues)
    occupation_encoded = one_hot_encode(occupation, occupationFeatureValues)
    relationShip_encoded = one_hot_encode(relationShip, relationShipFeatureValues)
    sex_encoded = one_hot_encode(sex, sexFeatureValues)

    # Combine all inputs
    data = [workClass_encoded, education_encoded, maritalStatus_encoded, occupation_encoded, 
            relationShip_encoded, sex_encoded, age, educationNo, capitalGain, capitalLoss, hourPerWeek]
    
    # Flatten the list efficiently
    data = np.concatenate([np.array(sublist).flatten() if isinstance(sublist, list) else np.array([sublist]) for sublist in data])

    # Load the model
    try:
        model = joblib.load('../salaryPredictionModel')  # Make sure the model file is in the same directory
        prediction = model.predict([data])[0]

        # Display Prediction
        if prediction == 1:
            st.subheader("Prediction: **Salary is greater than 50K** 💰")
        else:
            st.subheader("Prediction: **Salary is less than 50K** 📉")
    
    except FileNotFoundError:
        st.error("Model file not found. Ensure 'salaryPredictionModel.pkl' is in the correct directory.")

    except Exception as e:
        st.error(f"An error occurred: {e}")
