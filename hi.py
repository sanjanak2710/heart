import numpy as np
import pickle
import streamlit as st
import joblib

model = joblib.load("final_model.pkl")

input_data=(63,1,3,145,233,1,0,150,0,2.3,0,0,1)

def heart_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person does not have a presence of heart disease'
    else:
      return 'The person does have a presence of heart disease'

def main():
    
    
    # giving a title
    st.title('Presenece Of Heart Disease Prediction Web App')
    
    
    # getting the input data from the user
    
    
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    resting_bp=st.text_input('resting bp')
    sc=st.text_input("serum cholestoral")
    fbs=st.text_input("fasting blood sugar")
    rer=st.text_input("resting electrocardiographic results (values 0,1,2)")
    mhr=st.text_input("maximum heart rate achieved")
    eia=st.text_input("exercise induced angina")
    oldpeak = st.text_input("exercise induced angina")
    slope=st.text_input("slope")
    thal=st.text_input("thal")
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Presenece Of Heart Disease test'):
        diagnosis = heart_prediction([age,sex,resting_bp,sc,fbs,rer,mhr,eia,oldpeak,slop,thal])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()