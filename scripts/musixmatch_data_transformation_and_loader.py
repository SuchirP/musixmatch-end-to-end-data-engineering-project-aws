import json
import boto3
from datetime import datetime
from io import StringIO
import pandas as pd


def album(data):
  track_list = []
  for row in data["message"]["body"]["track_list"]:
    track_id = row["track"]["track_id"]
    track_name = row["track"]["track_name"]
    track_rating = row["track"]["track_rating"]
    artist_name = row["track"]["artist_name"]
    artist_id = row["track"]["artist_id"]
    track_share_url = row["track"]["track_share_url"]
    if row["track"]["primary_genres"]["music_genre_list"]:
      music_genre_name = row["track"]["primary_genres"]["music_genre_list"][0][
          "music_genre"]["music_genre_name"]
    else:
      music_genre_name = "N/A"  # If primary genres are not available
    track_element = {
        'track_id': track_id,
        'track_name': track_name,
        'rating': track_rating,
        'artist_name': artist_name,
        'artist_id': artist_id,
        "track_share_url": track_share_url,
        "music_genre": music_genre_name
    }
    track_list.append(track_element)
  return track_list


def lambda_handler(event, context):
  s3 = boto3.client('s3')
  Bucket = "mxm-etl-project-bucketname"
  Key = "raw_data/tobe_processed/"

  mxm_data = []
  mxm_keys = []
  for file in s3.list_objects(Bucket=Bucket, Prefix=Key)['Contents']:
    file_key = (file['Key'])
    if file_key.split('.')[-1] == 'json':
      response = s3.get_object(Bucket=Bucket, Key=file_key)
      content = response['Body']
      jsonObject = json.loads(content.read())
      mxm_data.append(jsonObject)
      mxm_keys.append(file_key)

  for data in mxm_data:
    track_list = album(data)

    album_df = pd.DataFrame.from_dict(track_list)

    album_key = "transformed_data/album_data/album_transformed_" + str(
        datetime.now()) + ".csv"
    album_buffer = StringIO()
    album_df.to_csv(album_buffer, index=False)
    album_content = album_buffer.getvalue()
    s3.put_object(Bucket=Bucket, Key=album_key, Body=album_content)

  s3_resource = boto3.resource('s3')
  for key in mxm_keys:
    copy_source = {'Bucket': Bucket, 'Key': key}
    s3_resource.meta.client.copy(copy_source, Bucket,
                                 'raw_data/processed/' + key.split("/")[-1])
    s3_resource.Object(Bucket, key).delete()
