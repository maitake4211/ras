import requests
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches
from io import BytesIO

subscription_key = '1629587b3f91451499d629e869f6d8c8'
assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

image_url = 'images\emotion_1.jpg'

header = {'Ocp-Apim-Subscription-Key': subscription_key }
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
    'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
}
data = {'url': image_url}
response = requests.post(face_api_url, params=params, headers=headers, json=data)
faces = response.json()

requests.post(emotion_recognition_url, headers=headers, json=image_data)

image_path = "images/emotion_1.jpg"
image_data = open(image_path, "rb").read()
