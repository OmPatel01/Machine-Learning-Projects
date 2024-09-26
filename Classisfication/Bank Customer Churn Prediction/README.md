# Bank Customer Churn Prediction

## Overview

This project aims to predict customer churn for a bank using machine learning techniques. Customer churn is when a customer stops using the bank's services, which is a significant concern for any financial institution. By predicting churn, the bank can proactively take steps to retain customers and improve business performance.

### Dataset

The dataset contains the following features:

| Feature           | Description                                                      |
|-------------------|------------------------------------------------------------------|
| `CustomerId`      | A unique identifier for each customer                            |
| `Surname`         | The customer's surname or last name                              |
| `CreditScore`     | The customer's credit score                                      |
| `Gender`          | The customer's gender (Male or Female)                           |
| `Age`             | The customer's age                                               |
| `Tenure`          | Number of years the customer has been with the bank              |
| `Balance`         | The customer's account balance                                   |
| `NumOfProducts`   | Number of bank products the customer uses (e.g., credit card)    |
| `HasCrCard`       | Whether the customer has a credit card (1 = Yes, 0 = No)         |
| `IsActiveMember`  | Whether the customer is an active member (1 = Yes, 0 = No)       |
| `EstimatedSalary` | The customer's estimated annual salary                           |
| `Exited`          | Whether the customer has churned (1 = Yes, 0 = No)               |

The target variable is `Exited`, indicating whether a customer churned or not.

## Models Used

Two approaches were used to handle the class imbalance in the target variable (`Exited`):

1. **Random Forest with SMOTE (Synthetic Minority Over-sampling Technique)**:
   SMOTE was used to balance the dataset by generating synthetic examples of the minority class (churners) during training. This ensures that the model is not biased towards predicting non-churners due to the imbalance.

2. **Random Forest with Class Weight Adjustment**:
   The class weights of the Random Forest model were adjusted to give higher importance to the minority class (churners), encouraging the model to better predict customers who are likely to churn.

## Evaluation Metrics

- **Precision**: The ratio of correctly predicted positive observations to the total predicted positives.
- **Recall**: The ratio of correctly predicted positive observations to all observations in the actual class.
- **F1-Score**: A balance between precision and recall.
- **Confusion Matrix**: To evaluate the number of true positives, true negatives, false positives, and false negatives.

## Results

### 1. Random Forest with SMOTE
- **Precision (Churners)**: 0.60
- **Recall (Churners)**: 0.63
- **Accuracy**: 84%
- **Mean Accuracy (Cross-Validation)**: 85.27%

### 2. Random Forest with Class Weight Adjustment
- **Precision (Churners)**: 0.56
- **Recall (Churners)**: 0.69
- **Accuracy**: 83%
- **Mean Accuracy (Cross-Validation)**: 81.57%

## When to Use Each Approach

### SMOTE + Random Forest:
- **When to use**: Use SMOTE when the business wants to **reduce false positives** (Type I errors). This is ideal if the cost of unnecessarily targeting non-churners is high, and you want to focus on precision (i.e., only targeting customers who are very likely to churn).
  
### Class Weight Adjustment + Random Forest:
- **When to use**: Use class weight adjustment when the business aims to **reduce false negatives** (Type II errors). This is appropriate when the cost of missing actual churners is significant, and the priority is to catch as many potential churners as possible, even if it leads to a higher false positive rate.

## Conclusion

Both models offer distinct advantages depending on the business use case:
- If **precision** is more critical, such as when the business wants to avoid spending resources on non-churners, the **SMOTE approach** is recommended.
- If **recall** is more important, such as when the business needs to retain every possible churner, the **class weight adjustment** approach is preferable.

Each model can be fine-tuned further based on the specific business priorities and cost considerations related to churn.

