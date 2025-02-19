from fastapi import FastAPI
from app.recommender import prediction

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Movie Recommendation API is running"}

@app.get("/recommend/{user_id}")
def get_recommendations(user_id: int, top_n: int = 5):
    recommemdations = prediction(user_id, top_n)
    return recommemdations