import json
import os
import joblib

from google.cloud import storage
from google.oauth2 import service_account
import pickle



def get_credentials():
    credentials_raw = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    if '.json' in credentials_raw:
        credentials_raw = open(credentials_raw).read()
    creds_json = json.loads(credentials_raw)
    creds_gcp = service_account.Credentials.from_service_account_info(creds_json)
    return creds_gcp


# def storage_upload(model_version=MODEL_VERSION, bucket=BUCKET_NAME, rm=False):
#     client = storage.Client().bucket(bucket)

#     storage_location = 'models/{}/versions/{}/{}'.format(
#         MODEL_NAME,
#         model_version,
#         'model.joblib')
#     blob = client.blob(storage_location)
#     blob.upload_from_filename('model.joblib')
#     print(colored("=> model.joblib uploaded to bucket {} inside {}".format(BUCKET_NAME, storage_location),
#                   "green"))
#     if rm:
#         os.remove('model.joblib')

BUCKET_NAME = "video-game-rec-99"
PROJECT_ID = "amazonreview-297414"

def download_model(bucket=BUCKET_NAME, rm=True, model_name = 'NaiveBayes'):
    creds = get_credentials()
    client = storage.Client(credentials=creds, project=PROJECT_ID).bucket(bucket)

    storage_location = 'Models/{}.joblib'.format(model_name)
    blob = client.blob(storage_location)
    blob.download_to_filename('{}.joblib'.format(model_name))
    print(f"=> pipeline downloaded from storage")
    model = joblib.load('{}.joblib'.format(model_name))
    if rm:
        os.remove('{}.joblib'.format(model_name))
    return model