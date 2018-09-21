subscription_key = '1629587b3f91451499d629e869f6d8c8'
assert subscription_key

emotion_recognition_url = "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"

headers  = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-Type": "application/octet-stream" }

image_path = "images/emotion_1.jpg"
image_data = open(image_path, "rb").read()

import requests
response = requests.post(emotion_recognition_url, headers=headers, data=image_data)
response.raise_for_status()
analysis = response.json()
analysis

header = {'Ocp-Apim-Subscription-Key': subscription_key }

data = {'url': image_url}

requests.post(emotion_recognition_url, headers=headers, json=image_data)
