from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from os import getenv
from dotenv import load_dotenv

load_dotenv()

KEY = getenv("AZURE_KEY")

ENDPOINT = getenv("AZURE_ENDPOINT")

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
