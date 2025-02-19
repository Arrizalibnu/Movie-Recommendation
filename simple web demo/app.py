import streamlit as st
import requests

API_URL = "http://3.27.188.84:8000/recommend"

st.title("🎬 Movie Recommendation System")
st.write("Masukkan User ID untuk mendapatkan rekomendasi film!")
user_id = st.text_input("Masukkan User ID:", "123")

if st.button("Get Recommendations"):
    if user_id:
        response = requests.get(f"{API_URL}/{user_id}?top_n=5")

        if response.status_code == 200:
            recommendations = response.json()
            st.subheader("🎥 Rekomendasi Film:")
            for movie in recommendations:
                st.write(f"- **{movie['title']}** (Movie ID: {movie['movieId_x']})")

        else:
            st.error("⚠️ Gagal mendapatkan rekomendasi. Periksa API server!")

    else:
        st.warning("⚠️ Masukkan User ID terlebih dahulu!")

