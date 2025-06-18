from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the dataset and similarity matrix from the pickle files
with open('newdf.pkl', 'rb') as file:
        newdf = pickle.load(file)
with open('similarity.pkl', 'rb') as file:
        similarity = pickle.load(file)


# Function to get movie recommendations
def recommend(movie_title):
    movie_title = movie_title.lower()  # Normalize to lowercase for comparison
    try:
        # Check if the movie exists in the dataset (case insensitive)
        movie_index = newdf[newdf['title'].str.lower() == movie_title].index[0]
        # Get top 5 similar movies, excluding the movie itself
        top_movies = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
        recommendations = [newdf.iloc[i[0]].title for i in top_movies]
        return recommendations
    except IndexError:
        # Movie not found
        return []

# MODIFIED ROUTE: Route to render the homepage (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route for movie recommendations
@app.route('/recommend', methods=['GET'])
def get_recommendations():
    movie = request.args.get('movie', default='', type=str)
    if movie:
        recommended_movies = recommend(movie)
        if recommended_movies:
            return jsonify({'recommendations': recommended_movies})
        else:
            return jsonify({'error': 'Movie not found in dataset. Please try a different title.'}), 404
    else:
        return jsonify({'error': 'Movie title is required.'}), 400


@app.route('/get_movie_suggestions', methods=['GET'])
def get_movie_suggestions():
    query = request.args.get('query', default='', type=str)
    suggestions = []
    if query:
        # Filter movie titles that start with or contain the query (case-insensitive)
        matching_movies = newdf[newdf['title'].str.lower().str.contains(query.lower(), na=False, regex=False)]['title'].tolist()
        suggestions = matching_movies[:10] # Limit to top 10 suggestions

    return jsonify({'suggestions': suggestions})

if __name__ == '__main__':
    # When running locally for testing, ensure 'newdf.pkl' and 'similarity.pkl' are present
    app.run(debug=True)
