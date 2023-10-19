import requests
import pandas as pd
from sqlalchemy import create_engine

def extract()-> dict:
    """Extracting the data from api url
    http://universities.hipolabs.com
    """
    API_URL = "http://universities.hipolabs.com/search?country=United+States"
    data = requests.get(API_URL).json()

    return data

print(extract())