import uvicorn

from fastapi import FastAPI

from student_performance_prediction import predict


app = FastAPI(title='score-prediction')


@app.post('/predict')
def perform_prediction(student: predict.Student) -> predict.PredictResponse:
    predicted_score = predict.predict_single(student.model_dump())
    return {
        'predicted_score': predicted_score
    }


if __name__ == '__main__':
    uvicorn.run('student_performance_prediction.serve:app', host='0.0.0.0', port=8000, reload=True)

