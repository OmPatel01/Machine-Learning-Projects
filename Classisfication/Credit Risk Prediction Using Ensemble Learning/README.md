# Credit Risk Prediction Using Ensemble Learning

This project focuses on building a machine learning model for credit risk prediction. The goal is to identify the likelihood of default based on key borrower attributes, enhancing decision-making in financial institutions. The project employs advanced techniques, including handling missing data, using multiple classifiers, and integrating a Voting Classifier for improved accuracy.

---

## Key Features

1. **Handling Missing Data**  
   - Missing values in the `loan_int_rate` column were imputed with the **median** to ensure a robust dataset for training.

2. **Modeling Techniques**  
   - Individual models like **Random Forest** and **Logistic Regression** were implemented.
   - A **Voting Classifier** was employed to combine the strengths of both models, achieving a balanced accuracy of **91%**.

3. **Performance Insights**  
   - The model emphasizes reducing **false positives** (approving risky loans) and **false negatives** (rejecting safe loans) to strike a balance between profitability and risk mitigation.

4. **Streamlit Integration**  
   - A user-friendly Streamlit web application allows users to interact with the model by inputting borrower details and visualizing predictions.

---

## Dataset Description

The dataset consists of the following attributes:

- **person_age**: Age of the borrower (in years).
- **person_income**: Annual income of the borrower (in USD).
- **person_home_ownership**: Type of home ownership (e.g., 'OWN', 'RENT').
- **loan_intent**: Purpose or intent of the loan (e.g., 'EDUCATION', 'DEBTCONSOLIDATION').
- **loan_grade**: Credit grade assigned to the loan (e.g., 'A', 'B', 'C').
- **loan_amnt**: The loan amount (in USD).
- **loan_int_rate**: Interest rate charged on the loan (percentage).
- **loan_status**: The loan status (0 for non-default, 1 for default).
- **loan_percent_income**: Percentage of income dedicated to the loan.
- **cb_person_default_on_file**: Historical default status (Y or N) of the borrower.
- **cb_person_cred_hist_length**: Length of the borrower's credit history (in years).

---

## Voting Classifier Insights
The Voting Classifier combines the predictions of Random Forest and Logistic Regression to balance precision and recall:
- **Random Forest**: Captures complex patterns but may overfit.
- **Logistic Regression**: Provides linear insights, complementing Random Forest.
- **Ensemble Outcome**: Improved overall accuracy and reduced bias towards false positives or negatives.

---

## Accuracy Metrics
- **Voting Classifier Accuracy**: **91%**
- **Precision**: Effective in identifying safe loans.
- **Recall**: Reduced false negatives, ensuring fewer safe loans are rejected.

---

## Streamlit Application

Explore the model interactively via the Streamlit app:  
[Credit Risk Prediction App](https://credit-risk-prediction1.streamlit.app/)

