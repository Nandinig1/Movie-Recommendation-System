
# 🎬 Movie Recommendation System (with Streamlit Web App)

## 🔍 Project Overview
This project is a machine learning-based **Movie Recommendation System** that suggests movies to users based on their preferences. It uses a **content-based filtering approach** based on movie genres from the **MovieLens dataset**.

The system is deployed as an interactive **Streamlit web app**, allowing users to enter a movie name and receive five similar movie recommendations instantly.

---

## 🛠️ Tools and Technologies Used
- **Language**: Python  
- **Platform**: Streamlit  
- **Libraries**: Pandas, Scikit-learn, TfidfVectorizer, Cosine Similarity  
- **Dataset**: MovieLens (ml-latest-small)

---

## 📁 Files Included
- `app.py` – Main Streamlit app file  
- `movies.csv` – Dataset used for recommendations  
- `README.md` – This project description file  
- `Movie_Recommendation_Report.pdf` –  report
-'  Movie_Recommendation_System.ipynb'-colab notebook
- `screenshots/` – App output examples

---

## 🚀 How to Run the App Locally

1. Install Streamlit (only once):
   ```
   pip install streamlit
   ```

2. Run the app:
   ```
   streamlit run app.py
   ```

3. A browser window will open at `http://localhost:8501` showing your recommendation system.

---

## 💡 How the Recommendation Works

- Uses **TF-IDF** to vectorize movie genres
- Calculates **cosine similarity** between movies
- Suggests the top 5 movies similar to the one the user enters

---

## 🧪 Example Output

> **Input**: Toy Story  
> **Output**:  
> - A Bug's Life  
> - Monsters, Inc.  
> - Finding Nemo  
> - Cars  
> - The Incredibles

---


