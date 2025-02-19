import numpy as np
import pandas as pd
from app.model_loader import load_model

model = load_model()

movies_df = pd.read_csv("data/df.csv")
all_ids_movie = movies_df["movieId_x"].unique()

def prediction(user_id, top_n=5):
  user_id = np.full(len(all_ids_movie), user_id).reshape(-1, 1)
  movie_id = all_ids_movie.reshape(-1, 1)

  prediction_ratings = model.predict([user_id, movie_id])

  recommendation = pd.DataFrame({
      "movieId_x" : all_ids_movie,
      "rating_pred": prediction_ratings.flatten()
  })

  recommendation = recommendation.sort_values(by= "rating_pred", ascending=False)
  recommendation = recommendation.merge(movies_df[["movieId_x", "title"]].drop_duplicates(), on="movieId_x", how="left")
  recommendation = recommendation.drop(["rating_pred"], axis=1)
  recommendation = recommendation.head(top_n)

  return recommendation.to_dict(orient="records")
