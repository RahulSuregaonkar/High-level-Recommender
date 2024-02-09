## Movie Recommendation System

This project is a movie recommendation system built using collaborative filtering techniques implemented with Keras and TensorFlow. Collaborative filtering is a method commonly used for recommender systems that generates predictions about the interests of a user by collecting preferences from many users. In this system, we use the preferences of multiple users to recommend movies to a target user based on similarities in movie preferences among users.
This Project Uses Django-Celery for countinuos Training of Machine Learning models based on user reaction for movies and gives recommendation instantaneously for every 5 ratings for the user 
Represents a cutting-edge approach to movie recommendation, leveraging Django-Celery to deliver personalized suggestions in real-time, keeping pace with users' evolving tastes and preferences.

## Vist Website
https://rahulrecommender.in.net/

## Colab Link
https://colab.research.google.com/drive/1o5-5Ehkr8tM36cSeYpVEOaDj5whrxTCu

### Technologies Used
- Django
- Celery
- Keras
- TensorFlow
- SVM
- HTML
- CSS
- HTMX
- BootStrap
- JavaScript

## Data Set
https://www.kaggle.com/datasets/omkarborikar/top-10000-popular-movies
https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=ratings.csv
https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=links.csv
https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv


### Features
- Provides movie recommendations based on collaborative filtering techniques.
- Real-time recommendation updates as the model is trained.
- Utilizes Django for web framework.
- Uses Celery for background worker processes.
- Dataset consists of top 10,000 TMDB movies.

## Getting Started

1. Clone the project and make it your own. Use branch `start` initially so we can all start in the same place.
```bash
git clone https://github.com/codingforentrepreneurs/recommender
cd recommender
git checkout start
rm -rf .git
git init .
git add --all
git commit -m "My recommender project"
```

2. Create virtual environment and activate it.

```bash
python3.8 -m venv venv
source venv/bin/activate
```
Use `.\venv\Scripts\activate` if on windows

3. Install requirements
```
(venv) python -m pip install pip --upgrade
(venv) python -m pip install -r requirements.txt
```

4. Open VSCode
```bash
code .
