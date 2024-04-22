## :mortar_board: Predicting Student Admission to University 

### Streamlit Web Application

Explore the interactive web application deployed using Streamlit [here](https://student-admission-prediction.streamlit.app/). Engage with the data and experience the predictive power firsthand!

### Summary

This project analyzes data related to student admission to universities. The dataset contains information on various factors that may influence admission decisions, such as GRE scores, TOEFL scores, university ratings, statement of purpose (SOP), letters of recommendation (LOR), cumulative grade point average (CGPA), research experience, and admission outcomes.

### Summary of Columns

1. **GRE Score**: 
   - Represents applicants' performance in the Graduate Record Examination, with an average score of approximately 316.47.

2. **TOEFL Score**: 
   - Reflects applicants' proficiency in the Test of English as a Foreign Language, with an average score of around 107.19.

3. **University Rating**: 
   - Provides ratings for the universities attended by applicants, with an average rating of approximately 3.11.

4. **SOP (Statement of Purpose)**: 
   - Conveys applicants' academic interests and motivations for pursuing higher education, with an average rating of 3.37.

5. **LOR (Letter of Recommendation)**: 
   - Offers insights into applicants' academic abilities and character, with an average rating of approximately 3.48.

6. **CGPA (Cumulative Grade Point Average)**: 
   - Represents applicants' cumulative grade point average, with an average score of 8.58.

### Outliers

No significant outliers were detected in any of the columns, indicating consistency and uniformity in the data distribution across all features.

### Modeling Approach

#### Feature Scaling:
- Applied standard scaling to all numerical features using the `StandardScaler` from scikit-learn to ensure features are on a similar scale, facilitating better convergence during model training.

#### Model Selection:
- Chose logistic regression as the classification algorithm due to its simplicity, efficiency, and interpretability, given the binary nature of the target variable (admitted or not admitted).

#### Pipeline Construction:
- Constructed a pipeline using scikit-learn's `Pipeline` class to streamline preprocessing and modeling steps.
- The pipeline encapsulates both preprocessing (scaling) and logistic regression modeling steps, ensuring consistent and sequential application of transformations.

### Evaluation Metrics

- **Accuracy**: 94%
- **Precision**: 91%
- **Recall**: 90%
- **F1-Score**: 91%
- **Confusion Matrix**: 
  - Correctly identified 41 negative cases and 53 positive cases. 
  - Mistakenly labeled 6 negative cases as positive and missed none of the positive cases.
- **ROC curve**: 
  - Indicates excellent performance with a high true positive rate and a low false positive rate, as indicated by the AUC of 0.94.

### Note

While the model demonstrates good performance, its generalizability may be limited due to the small dataset size (500 records). Acquiring more data could enhance the model's ability to capture underlying patterns and relationships, potentially improving its overall performance.
