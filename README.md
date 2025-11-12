# 1. Problem statement

### Student Performance Prediction (SPP)**

This project aims to analyze and predict student academic performance using machine learning. By leveraging the Student Performance Factors dataset from Kaggle, the study explores how various demographic, social, and educational factors influence students’ success in their studies.

The main objective is to develop a predictive model capable of identifying key factors that contribute to academic outcomes, providing valuable insights for educators, policymakers, and institutions seeking to improve learning effectiveness.

The project includes data preprocessing, exploratory data analysis (EDA), feature selection, model training, and performance evaluation using multiple ML algorithms. The final model can be used to forecast student performance and assist in early intervention strategies for at-risk learners.

**Project summary**:

Problem: predict student academic performance.
Target: 'Exam Score'
Objective: this project aims to predict students at risk of low academic performance using demographic, social, and educational data.
Evaluation metric: RMSE
How the model can be used: the model can serve as an early warning system — enabling educators and decision-makers to take proactive, data-informed actions that improve learning outcomes and reduce dropout or failure rates.

**Project structure**
```
.
├── Dockerfile
├── images-Readme
│   └── image.png
├── pyproject.toml
├── README.md
├── src
│   ├── data
│   │   └── StudentPerformanceFactors.csv
│   └── student_performance_prediction
│       ├── __init__.py
│       ├── main.ipynb
│       ├── model.bin
│       ├── predict.py
│       ├── serve.py
│       └── train.py
└── uv.lock
```

# 2. Dataset description

| Data | Definition | Type | Values
| ----------- | ----------- | ----------- | ----------- |
| Hours Studied | Number of study hours per week | integer | Minimun value: 0 |
| Attendance | Percentage of attendance throughout the term | integer | Minimun value: 0, Maximun value: 100 |
| Parental Involvement | Level of parental support in academics | string | Low, Medium, High |
| Access to Resources | Availability of academic resources like books or internet | string | Low, Medium, High |
| Extracurricular Activities | Whether the student participates in outside of their regular academic curriculum | string | Yes, No |
| Sleep Hours | Average hours of sleep per day | integer  | Minimun value: 0 |
| Previous Scores | Average of previous academic scores | integer | Minimun value: 0, Maximun value: 100 |
| Motivation Level | Student’s motivation level | string | Low, Medium, High |
| Internet Access | Whether the student has access to the internet | string | Yes, No |
| Tutoring Sessions | Number of tutoring sessions per week | integer | Minimun value: 0 |
| Family Income | Family income level | string | Low, Medium, High |
| Teacher Quality | Overall perceived teacher quality | string | Low, Medium, High |
| School Type | Type of school | string | Public, Private |
| Peer Influence | Influence of peers on academic performance | string | Negative, Neutral, Positive |
| Physical Activity | Hours of physical activity per week | integer | Minimun value: 0 |
| Learning Disabilities | Presence of any learning disabilities | string | Yes, No |


# 2. Dataset description

| Data | Definition | Type | Values
| ----------- | ----------- | ----------- | ----------- |
| Hours Studied | Number of study hours per week | integer | Minimun value: 0 |
| Attendance | Percentage of attendance throughout the term | integer | Minimun value: 0, Maximun value: 100 |
| Parental Involvement | Level of parental support in academics | string | Low, Medium, High |
| Access to Resources | Availability of academic resources like books or internet | string | Low, Medium, High |
| Extracurricular Activities | Whether the student participates in outside of their regular academic curriculum | string | Yes, No |
| Sleep Hours | Average hours of sleep per day | integer  | Minimun value: 0 |
| Previous Scores | Average of previous academic scores | integer | Minimun value: 0, Maximun value: 100 |
| Motivation Level | Student’s motivation level | string | Low, Medium, High |
| Internet Access | Whether the student has access to the internet | string | Yes, No |
| Tutoring Sessions | Number of tutoring sessions per week | integer | Minimun value: 0 |
| Family Income | Family income level | string | Low, Medium, High |
| Teacher Quality | Overall perceived teacher quality | string | Low, Medium, High |
| School Type | Type of school | string | Public, Private |
| Peer Influence | Influence of peers on academic performance | string | Negative, Neutral, Positive |
| Physical Activity | Hours of physical activity per week | integer | Minimun value: 0 |
| Learning Disabilities | Presence of any learning disabilities | string | Yes, No |
| Parental Education Level | Highest education level of parents | string | High School, College, Postgraduate |
| Distance From Home | Distance between home and school | string | Near, Moderate, Far |
| Gender | Student’s gender | string | Male, Female |
| Exam Score | Final exam score (0–100) — the target variable | integer | Minimun value: 0, Maximun value: 100 |

Data from: https://www.kaggle.com/datasets/mosapabdelghany/student-performance-factors-dataset
  

# 3. EDA summary

a. Distribution of students’ exam scores.

![Exam score distribution](image.png)

This histogram shows:

* Most students scored between 65 and 75, forming a clear peak around 70 — that’s where the highest frequency occurs.

* Very few students scored below 60 or above 80, which means low and high scores are rare.

* The distribution is left-skewed (negatively skewed) — it tails slightly toward higher scores, indicating that most students performed fairly well, with only a few exceptional high achievers (outliers).

b. Missing values.

During the initial data exploration, three categorical features were found to contain missing values:

| Feature | Missing records |
| ----------- | ----------- |
| teacher_quality | 78 |
| parental_education_level | 90 | 
| distance_from_home | 67 | 
in total, 229 records where found with one of more columns with missing values.

Since these missing values represent only a small portion of the dataset (approximately 3.5% of all records) and all affected columns are categorical, the decision was made to replace the missing entries with the category "Unknown".


# 4. Modeling approach & metrics

The following models were evaluated:

Linear Regression: baseline model for performance comparison.
Decision Tree Regressor
Random Forest Regressor
XGBoost Regressor

Hyperparameter tuning was performed for the Decision Tree Regressor, Random Forest Regressor and XGBoost Regressor models to identify the best configurations.

Model performance was assessed using the Root Mean Squared Error (RMSE) metric, which measures the average magnitude of prediction errors (lower values indicate better accuracy).

| Model	| RMSE |
| ----------- | ----------- |
| Linear Regression | 2.263 |
| Decision Tree Regressor | 2.870 |
| Random Forest Regressor | 2.518 |
| XGBoost | 2.303 |

Among all tested models, Linear Regression achieved the lowest RMSE (2.263), closely followed by XGBoost (2.303).

# 5. How to run

## Locally
### Prerequisites
- Python 3.11+
- uv (to create and manage the virtual environment)

### Clone the repository
 
```bash
$ git clone https://github.com/<your-username>/<your-repo-name>.git`  
$ cd <your-repo-name>
```

### Set Up the Environment
```bash
$ uv venv
$ source .venv/bin/activate      # On Linux/Mac
# or
$ .venv\Scripts\activate         # On Windows
```

### Install Dependencies
```bash
$ uv pip install -e .
```
This will automatically read the dependencies listed in pyproject.toml and install them in your environment.
### Run the Project

- To start the prediction API:  
```bash
$ python src/student_performance_prediction/predict.py
```
This script launches a FastAPI application that loads the trained model (model.bin) and provides an endpoint to predict student exam scores based on input data (JSON format).

### Train the model (additional)
- To train the model:  
```bash
$ python src/student_performance_prediction/train.py
```
This script loads the dataset, trains the model, and creates the serialized model file model.bin using pickle.

## Build and Run the Application Using Docker
### Prerequisites
- Docker

### Build the Docker Image
From the root directory of the project, build the image using:
```bash
$ docker build -t student-score-prediction.
```
This command creates a Docker image named student-score-prediction based on the configuration in the Dockerfile.

### Run the Container
Once the image has been built, start a container using:
```bash
$ docker run -it --rm -p 8000:8000 student-score-prediction
```
This command launches a Docker container that allow predict.py to run and make score predictions.

# Making request:

## Via curl
Example request:
```bash
$ curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "hours_studied": 15, 
    "attendance": 66, 
    "parental_involvement": "medium", 
    "access_to_resources": "low", 
    "extracurricular_activities": "yes", 
    "sleep_hours": 4, 
    "previous_scores": 90, 
    "motivation_level": "low", 
    "internet_access": "yes", 
    "tutoring_sessions": 2, 
    "family_income": "medium", 
    "teacher_quality": "high", 
    "school_type": "public", 
    "peer_influence": "negative", 
    "physical_activity": 7, 
    "learning_disabilities": "no", 
    "parental_education_level": "college", 
    "distance_from_home": "far", 
    "gender": "female"
}'
```
## Browser



## Running the python code for testing the app.
```bash
$ python src/student_performance_prediction/serve.py
```
This script sends a predifined JSON request to the FastAPI app and prints the predicted score in the console.  



# 6. API usage example



# 7. Known limitations / next steps


