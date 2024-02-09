## Movie Recommendation System

This project is a movie recommendation system built using collaborative filtering techniques implemented with Keras and TensorFlow. Collaborative filtering is a method commonly used for recommender systems that generates predictions about the interests of a user by collecting preferences from many users. In this system, we use the preferences of multiple users to recommend movies to a target user based on similarities in movie preferences among users.

## Vist Website
https://rahulrecommender.in.net/

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
