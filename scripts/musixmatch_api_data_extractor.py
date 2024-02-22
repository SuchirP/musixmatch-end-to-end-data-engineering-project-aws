import json
import os
import requests
import boto3
from datetime import datetime


def lambda_handler(event, context):
  musixmatch_api_key = os.environ.get('musixmatch_api_key')
  url = f"https://api.musixmatch.com/ws/1.1/chart.tracks.get?chart_name=mxmweekly&page=1&page_size=50&country=us&f_has_lyrics=1&apikey={musixmatch_api_key}"

  # Make a GET request to the API
  response = requests.get(url)

  # Check if the request was successful
  if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    # Pretty print the JSON data with indentation
    print(json.dumps(data, indent=4))
  else:
    print("Error:", response.status_code)

  client = boto3.client('s3')

  filename = "mxm_raw_" + str(datetime.now()) + ".json"

  client.put_object(Bucket="mxm-etl-project-suchir",
                    Key="raw_data/tobe_processed/" + filename,
                    Body=json.dumps(data))
