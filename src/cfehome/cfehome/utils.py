from faker import Faker
import csv
from pprint import pprint
import datetime
from django.conf import settings
import logging


MOVIE_METADATA_CSV = settings.DATA_DIR / "10000 Movies Data"


def validate_date_str(date_text):
    try:
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
    except:
        return None
    return date_text



def load_movie_data(limit=1):
    dataset = []
    try:
        with open(MOVIE_METADATA_CSV, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                _id = row.get("Movie_id")
                poster = row.get("poster_path")
                try:
                    _id = int(_id)
                except ValueError:
                    _id = None

                release_date = validate_date_str(row.get('release_date'))
                data = {
                    "id": _id,
                    "title": row.get('title'),
                    "overview": row.get("overview"),
                    "release_date": release_date,
                    "poster_path": poster
                }
                dataset.append(data)
                if i + 1 > limit:
                    break
    except FileNotFoundError:
        logging.error(f"CSV file '{MOVIE_METADATA_CSV}' not found.")
    except UnicodeDecodeError as e:
        logging.error(f"Error decoding CSV file: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

    return dataset



def get_fake_profiles(count=10):
    fake = Faker()
    user_data = []

    for _ in range(count):
        profile = fake.profile()
        data = {
            "username": profile.get('username'),
            "email": profile.get('mail'),
            "is_active": True
        }
        if 'name' in profile:
            fname, lname = profile.get('name').split(" ")[:2]
            data['first_name'] = fname
            data['last_name'] = lname
            
        user_data.append(data)
    return user_data