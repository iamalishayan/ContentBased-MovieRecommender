# Content-Based Movie Recommendation System

This is a simple **Movie Recommender System** that suggests similar movies based on a user’s selection. It uses **content-based filtering** with cosine similarity over vectorized movie metadata (like genres, keywords, and descriptions). A basic web interface was created using Flask for user interaction.

---

## Dataset

- **Source:** Movie metadata from [TMDB](https://www.themoviedb.org/) (via Kaggle)
- The data was cleaned and preprocessed using Pandas.
- Features used for similarity:  
  - `genres`  
  - `keywords`  
  - `overview` (description)

---

## Libraries Used

- `pandas`, `numpy` – data manipulation and wrangling  
- `scikit-learn` – cosine similarity & vectorization  
- `nltk` – text preprocessing  
- `flask` – backend for serving recommendations  
- `pickle` – for saving/loading the similarity matrix

---

## Recommendation Logic

- Extracted important text-based features.
- Combined them into a single string representation for each movie.
- Vectorized text using **TfidfVectorizer**.
- Computed **cosine similarity** between all movies.
- Given a movie, returned the top 5 most similar ones.

---

## Web App

- Created a simple Flask app (`app.py`)  
- Users can:
  - Select a movie
  - View recommended movies instantly
- Minimalistic and easy-to-use interface

---

## 📥 Downloading the Model File

The `similarity.pkl` file is too large to include in the repo.

To run the recommender system locally, download the file using:

```bash
- pip install gdown
- python download_model.py
```

---

## 🧠 Author

- **Ali Shayan** – [GitHub Profile](https://github.com/iamalishayan)

---

Feel free to fork the repo, suggest improvements, or report issues!