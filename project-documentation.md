## 1. Problem statement

### Student Performance Prediction (SPP)

The main objective is to develop a predictive model capable of identifying key factors that contribute to academic outcomes, providing valuable insights for educators, policymakers, and institutions seeking to improve learning effectiveness.  

The project includes data preprocessing, exploratory data analysis (EDA), feature selection, model training, and performance evaluation using multiple ML algorithms. The final model can be used to forecast student performance and assist in early intervention strategies for at-risk learners.  

### Problem summary

Problem: predict student academic performance.  
Target: 'Exam Score'.  
Evaluation metric: RMSE.  
How the model can be used: the model can serve as an early warning system — enabling educators and decision-makers to take proactive, data-informed actions that improve learning outcomes and reduce dropout or failure rates.  


## 2. Dataset description

| Data | Definition | Type | Values
| ----------- | ----------- | ----------- | ----------- |
| Hours Studied | Number of study hours per week | Numerical: integer | Minimun value: 0 |
| Attendance | Percentage of attendance throughout the term | Numerical: integer | Minimun value: 0, Maximun value: 100 |
| Parental Involvement | Level of parental support in academics | Categorical: string | Low, Medium, High |
| Access to Resources | Availability of academic resources like books or internet | Categorical: string | Low, Medium, High |
| Extracurricular Activities | Whether the student participates in outside of their regular academic curriculum | Categorical: string | Yes, No |
| Sleep Hours | Average hours of sleep per day | Numerical: integer  | Minimun value: 0 |
| Previous Scores | Average of previous academic scores | Numerical: integer | Minimun value: 0, Maximun value: 100 |
| Motivation Level | Student’s motivation level | Categorical: string | Low, Medium, High |
| Internet Access | Whether the student has access to the internet | Categorical: string | Yes, No |
| Tutoring Sessions | Number of tutoring sessions per week | Numerical: integer | Minimun value: 0 |
| Family Income | Family income level | Categorical: string | Low, Medium, High |
| Teacher Quality | Overall perceived teacher quality | Categorical: string | Low, Medium, High |
| School Type | Type of school | Categorical: string | Public, Private |
| Peer Influence | Influence of peers on academic performance | Categorical: string | Negative, Neutral, Positive |
| Physical Activity | Hours of physical activity per week | Numerical: integer | Minimun value: 0 |
| Learning Disabilities | Presence of any learning disabilities | Categorical: string | Yes, No |
| Parental Education Level | Highest education level of parents | Categorical: string | High School, College, Postgraduate |
| Distance From Home | Distance between home and school | Categorical: string | Near, Moderate, Far |
| Gender | Student’s gender | Categorical: string | Male, Female |
| Exam Score | Final exam score (0–100) — the target variable | Target: integer | Minimun value: 0, Maximun value: 100 |

Data from: https://www.kaggle.com/datasets/mosapabdelghany/student-performance-factors-dataset
  

## 3. EDA summary

### Dataset Overview

The dataset contains 6607 student records and 19 features, being most of them categorical.

The target variable is Exam Score, a continuous value from 0 to 100.
Note: One record was found to have a score of 101. It was dropped.

See **2. Data description** for a further description.

### Missing values.

During the initial data exploration, three categorical features were found to contain missing values:

| Feature | Missing records |
| ----------- | ----------- |
| teacher_quality | 78 |
| parental_education_level | 90 | 
| distance_from_home | 67 | 

In total, 229 records where found with one of these columns with missing values.  

Since these missing values represent only a small portion of the dataset (approximately 3.5% of all records) and all affected columns are categorical, the decision was made to replace the missing entries with the category "Unknown".  

### Target Variable Distribution

![Exam score distribution](images-Readme/target-distribution.png)
This histogram shows:

* Most students scored between 60 and 75, forming a clear peak around 67-69 (where the highest frequency occurs).

* Very few students scored below 59 or above 76, which means low and high scores are rare.

* The distribution is a roughly bell-shaped distribution centered in the 67-69, with the majority of students performing close to this central range, with only a few exceptional high achievers (outliers).

Note: A record with Exam score of 101 was removed from the dataset.

### Features Distributions

![Features distributions](images-Readme/features-distributions.png)

The bar charts above illustrate how each categorical feature is distributed across the dataset. A few important patterns emerge:


- Parental involvement: fairly spread but slightly concentrated in medium involvement (around 50%).
- Access to resources: most students fall under the medium or high category (near to 50%).  
- Extracurricular activities: slightly more yes than no.  
- Motivational level: fairly spread but slightly concentrated in medium involvement (around 50%).
- Internet access: a very large majority of students have internet access.  
- Family income: concentrated in medium and low brackets (around 40% each).  
- Teacher quality: middle level ("medium") appear most common (close to 60%).  
- School type: most students attend public schools (close to 70%).  
Learning disabilities: most students report no learning disabilities (over 90%).  
- Peer influence: roughly even across positive and neutral (around 40% each). 
- Learning disabilities: a very large majority of students (around 85%) report no learning disabilities.  
- Parental education level: fairly distributed between parents with high school (around 48%), college education (30%) and postgraduated (22%).  
- Distannce from home: the majority of students live near school (around 58%), with fewer in moderate (30%) and far (less than 10%).
- Gender: the distribution shows a higher number of male students than female, but not drastically imbalanced.

Many categorical features show skewed distributions, where one category dominates.  
This is common and not necessarily problematic, but it may be harder to learn about patterns related to small groups (e.g., living far from school or no internet access).

Despite imbalances, all categorical variables together can help the model to understand student performance drivers.

### Features importance

| Categorical feature | mutual info with exam_score |
| ----- | ----- |
| access_to_resources | 0.027738 |
| parental_involvement | 0.022817 |
| parental_education_level | 0.016276 |
| peer_influence | 0.013170 |
| distance_from_home | 0.013117 |
| family_income | 0.011312 |
| motivation_level | 0.010994 |
| teacher_quality | 0.010982 |
| learning_disabilities | 0.008993 |
| extracurricular_activities | 0.006423 |
| gender | 0.004688 |
| internet_access | 0.004536 |
| school_type | 0.003773 |

Access to resources and Parental involvement show the highest MI scores, suggesting they provide the most insight into student performance.

On the other hand, Gender, Intenet access and School type contribute only a small amount

After checking the scores, it seems that performance depends on multiple interacting factors rather than single dominant features.

### Correlations

![Correlation](images-Readme/correlation.png)

Attendance and hours studied are the two most predictive numerical features in terms of linear relationship with exam scores.

The low correlations among independent variables suggest a clean dataset with minimal redundancy, which is ideal for modeling.

## 4. Modeling approach & metrics

The following models were evaluated:

- Linear Regression: baseline model for performance comparison.
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

Hyperparameter tuning was performed for the Decision Tree Regressor, Random Forest Regressor and XGBoost Regressor models to identify the best configurations.

Model performance was assessed using the Root Mean Squared Error (RMSE) metric, which measures the average magnitude of prediction errors (lower values indicate better accuracy).

| Model	| RMSE |
| ----------- | ----------- |
| Linear Regression | 1.993 |
| Decision Tree Regressor | 2.707 |
| Random Forest Regressor | 2.309 |
| XGBoost | 2.071 |

Among all tested models, Linear Regression achieved the lowest RMSE (1.993), closely followed by XGBoost (2.071).

### Model Evaluation Summary

To assess the model’s ability to generalize to unseen data, a 5-fold cross-validation procedure was applied. The resulting RMSE scores and the data associated with across the folds were:  

| 5-fold RMSE scores | Scores mean | Standard deviation | Full training RMSE |
| ----------- | ----------- | ----------- | ----------- |
| 2.035 - 2.400 - 2.202 - 2.204 - 1.718 | 2.112 | 0.2283 | 1.521 |

The model shows stable performance across folds, with a relatively small standard deviation (0.2283), indicating low variance. The full-training RMSE (1.521) is lower than the cross-validated mean RMSE, which is expected since the model trains on more data. Overall, the results suggest the model generalizes reasonably well, without strong signs of overfitting.




# 7. Known limitations / next steps

The model is largely influenced by the high presence of middle–lower income student populations (around 80% of students with low and medium family incomes  and near 70% comes from public schools).

Also, many features are self-reported (e.g., motivation, peer influence), which may contain bias or measurement error and reduce predictability.

The dataset reflects only a single moment in time. Student performance is dynamic and often changes across semesters, which cannot be captured here.

Next step: we could suggest to try more another models like Gradient Boosting or Neural Networks.

