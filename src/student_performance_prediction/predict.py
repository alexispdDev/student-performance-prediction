import os
import pickle

from pydantic import BaseModel, Field
from typing import Literal


class Student(BaseModel):
    hours_studied: int = Field(..., ge=0)
    attendance: int = Field(..., ge=0, le=100)
    parental_involvement: Literal['low', 'medium', 'high']
    access_to_resources: Literal['low', 'medium', 'high']
    extracurricular_activities: Literal['yes', 'no']
    sleep_hours: int = Field(..., ge=0)
    previous_scores: int = Field(..., ge=0, le=100)
    motivation_level: Literal['low', 'medium', 'high']
    internet_access: Literal['yes', 'no']
    tutoring_sessions: int = Field(..., ge=0)
    family_income: Literal['low', 'medium', 'high']
    teacher_quality: Literal['low', 'medium', 'high']
    school_type: Literal['public', 'private']
    peer_influence: Literal['negative', 'neutral', 'positive']
    physical_activity: int = Field(..., ge=0)
    learning_disabilities: Literal['yes', 'no']
    parental_education_level: Literal['high_school', 'college', 'postgraduate']
    distance_from_home: Literal['near', 'moderate', 'far']
    gender: Literal['male', 'female']


class PredictResponse(BaseModel):
    predicted_score: float
    

MODEL_PATH = os.environ.get("MODEL_PATH", 'src/student_performance_prediction/model.bin')
with open(MODEL_PATH, 'rb') as f_in:
    pipeline = pickle.load(f_in)


def predict_single(student) -> PredictResponse:
    predicted_score = pipeline.predict(student)[0]
    return float(predicted_score)
