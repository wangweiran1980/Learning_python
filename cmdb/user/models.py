import json
from django.db import models

# Create your models here.

DATA_FILE = './data.json'


def get_users() -> list[dict, str]:
    try:
        with open(DATA_FILE, 'r') as f:
            users = json.load(f)
    except FileNotFoundError as err:
        return {}, err
    return users, ''
