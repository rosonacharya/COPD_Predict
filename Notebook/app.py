# Import the libraries
import pandas as pd
import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder
with open('Best_Model.pkl','rb') as f:
    model = pickle.load(f)

# Streamlit App
def main():
    st.title("Chronic Obstructive Pulmonary Disease (COPD)  Predicition in Nepal")

    # User input
    st.header("Provide below information for Predicition!!!")
    Age  = age = st.slider("Age", 30, 80, 50)
    Biomass_Fuel_Exposure=st.selectbox("Biomass Fuel Exposure", ["Yes", "No"])
    Occupational_Exposure=st.selectbox("Occupational Exposure", ["Yes", "No"])
    Family_History_COPD =st.selectbox("Family History", ["Yes", "No"])
    BMI=bmi = st.slider("BMI", 10, 40, 25)
    Air_Pollution_Level=st.slider("Air Pollution Level", 0, 300, 50)
    Respiratory_Infections_Childhood =st.selectbox("Respiratory Infections in Childhood", ["Yes", "No"])
    NewGender=st.selectbox("Gender", ["Male", "Female"])
    Smoking_Status_encoded=st.selectbox("Smoking Status", ["Current", "Former", "Never"])
    Location_encoded = st.selectbox("Location", ["Kathmandu", "Pokhara", "Biratnagar", "Lalitpur", "Birgunj", 'Chitan', "Hetauda", "Dharan", "Butwal"])


    # Process the input data
    input_data = {
        'Age': [Age],
        'Biomass_Fuel_Exposure': [Biomass_Fuel_Exposure],
        'Occupational_Exposure': [Occupational_Exposure],
        'Family_History_COPD': [Family_History_COPD],
        'BMI': [BMI],
        'Air_Pollution_Level': [Air_Pollution_Level],
        'Respiratory_Infections_Childhood': [Respiratory_Infections_Childhood],
        'NewGender':[NewGender],
        'Smoking_Status_encoded': [Smoking_Status_encoded],
        'Location_encoded':[Location_encoded]       
    }

    # Convert the data to a dataframe
    input_df = pd.DataFrame(input_data)
    # Encoding
    input_df['Age']=input_df['Age']
    input_df['Biomass_Fuel_Exposure'] = input_df["Biomass_Fuel_Exposure"].map({'Yes': 1, 'No': 0})
    input_df['Occupational_Exposure'] = input_df["Occupational_Exposure"].map({'Yes': 1, 'No': 0})
    input_df['Family_History_COPD'] = input_df["Family_History_COPD"].map({'Yes': 1, 'No': 0})
    input_df['BMI']=input_df['BMI']
    input_df['Respiratory_Infections_Childhood'] = input_df["Respiratory_Infections_Childhood"].map({'Yes': 1, 'No': 0})
    input_df['NewGender'] = input_df["NewGender"].map({'Male': 1, 'Female': 0})
    input_df['Smoking_Status_encoded'] = input_df['Smoking_Status_encoded'].map({'Current': 1, 'Former': 0.5, 'Never': 0})
    le = LabelEncoder()
    input_df['Location_encoded'] = le.fit_transform(input_df['Location_encoded'])
    
 
    if st.button("Predict"):
        prediction = model.predict(input_df)
        if prediction[0] == 1:
            st.write("Prediction: COPD Detected")
        else:
            st.write("Prediction: No COPD Detected")
    
   
    

    
if __name__ == "__main__":
    main()