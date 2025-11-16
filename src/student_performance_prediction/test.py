import requests

url = 'http://localhost:8000/predict'

student = {
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
}

r = requests.post(url, json=student)
print(r.status_code)

prediction_response = r.json()
print('response: ', prediction_response)
