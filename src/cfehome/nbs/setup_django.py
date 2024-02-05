import os
import sys
import django

# Define the Django settings module
DJANGO_SETTINGS_MODULE = "cfehome.settings"

# Define the path to your Django project directory
PWD = "C:/Users/ronis/Desktop/Recommender/recommender/src/cfehome"

def init():
    os.chdir(PWD)
    sys.path.insert(0, PWD)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    django.setup()