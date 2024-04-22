import streamlit as st
import numpy as np
import pickle
import pandas as pd

pipe = pickle.load(open('pipe.pkl', 'rb'))

def main():
    st.title('Student Admission Prediction')

    # GRE score
    gre = st.number_input('GRE Score', min_value=0, max_value=340, value=0, step=1)

    # TOEFL score
    toefl = st.number_input('TOEFL Score', min_value=0, max_value=120, value=0, step=1)

    # University Rating
    university_rating = st.number_input('University Rating', min_value=1, max_value=5, value=1, step=1)

    # SOP
    sop = st.number_input('SOP', min_value=1.0, max_value=5.0, value=1.0, step=0.1)

    # LOR
    lor = st.number_input('LOR', min_value=1.0, max_value=5.0, value=1.0, step=0.1)

    # CGPA
    cgpa = st.number_input('CGPA', min_value=1.0, max_value=10.0, value=1.0, step=0.1)

    # Research
    research = st.selectbox('Research', ['Yes', 'No'])

    if st.button('Predict'):
        research = 1 if research == 'Yes' else 0

        # Prepare input data as a DataFrame
        input_data = pd.DataFrame({
            'GRE Score': [gre],
            'TOEFL Score': [toefl],
            'University Rating': [university_rating],
            'SOP': [sop],
            'LOR ': [lor],
            'CGPA': [cgpa],
            'Research': [research]
        })

        # Make prediction using the pre-trained pipeline
        prediction = pipe.predict(input_data)[0]

        # Display the prediction result
        if prediction == 1:
            st.title('Prediction: Admitted')
        else:
            st.title('Prediction: Not Admitted')

if __name__ == "__main__":
    main()
