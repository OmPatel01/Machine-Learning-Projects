# 🩺 Diabetes Risk Prediction

This project aims to predict the risk of diabetes using a machine learning model trained on a dataset with various health-related features. The project explores the use of Decision Tree and Random Forest classifiers to determine the likelihood of diabetes based on the given inputs.

## 📊 Dataset Features

The dataset consists of the following features:

1. **Age**: Age of the individual (numeric).
2. **Gender**: Gender of the individual (binary: Male/Female).
3. **Polyuria**: Frequent urination (binary: Yes/No).
4. **Polydipsia**: Excessive thirst (binary: Yes/No).
5. **Sudden weight loss**: Sudden weight loss (binary: Yes/No).
6. **Weakness**: Generalized weakness (binary: Yes/No).
7. **Polyphagia**: Excessive hunger (binary: Yes/No).
8. **Genital thrush**: Fungal infection around the genital area (binary: Yes/No).
9. **Visual blurring**: Blurred vision (binary: Yes/No).
10. **Itching**: Generalized itching (binary: Yes/No).
11. **Irritability**: Increased irritability (binary: Yes/No).
12. **Delayed healing**: Delay in healing wounds (binary: Yes/No).
13. **Partial paresis**: Partial muscle weakness (binary: Yes/No).
14. **Muscle stiffness**: Stiffness in muscles (binary: Yes/No).
15. **Alopecia**: Hair loss (binary: Yes/No).
16. **Obesity**: Obesity status (binary: Yes/No).
17. **Class**: The target variable indicating the presence of diabetes (binary: Positive/Negative).

## 🛠️ Model Training

### Decision Tree

The first model trained was a Decision Tree classifier. However, the model exhibited signs of overfitting, achieving perfect accuracy on the training set but performing less effectively on the test set.

### Random Forest

Next, a Random Forest classifier was trained to mitigate the overfitting observed with the Decision Tree. Although the Random Forest model performed better, it still showed signs of overfitting.

### Cross-Validation

To further improve the model's generalization, a 10-fold cross-validation was performed. This technique helped in assessing the model's performance across different subsets of the data, providing a more reliable estimate of its accuracy.

### 📈 Model Evaluation

The ROC AUC curve was used to evaluate the performance of both models. The Random Forest classifier demonstrated better performance compared to the Decision Tree, as indicated by a higher AUC score.

## 📌 Conclusion

The Random Forest model, after applying cross-validation, outperformed the Decision Tree model in predicting diabetes risk. Despite initial signs of overfitting, the use of cross-validation helped in achieving a more robust model.
