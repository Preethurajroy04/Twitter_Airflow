import requests
import pandas as pd
import s3fs

def run_twitter_etl():
    # Get the file ID from the shareable link
    file_id = "1_VxpZ3ZWaX16m3l1Gipfpr5LgRkA-R1B"

    # Create the URL to download the file
    url = "https://drive.google.com/uc?export=download&id=" + file_id

    # Download the file
    response = requests.get(url)

    # Convert the file to a Pandas dataframe
    df = pd.read_csv(response.content)


    df.to_csv("s3://preet-airflow-bucket/elon_musk_tweets.csv")