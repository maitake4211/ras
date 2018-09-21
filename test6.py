# -*- coding: UTF-8 -*-
#http://qiita.com/Algebra_nobu/items/a488fdf8c41277432ff3
import cv2
import os
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches
from io import BytesIO
import requests

subscription_key = "1629587b3f91451499d629e869f6d8c8"
assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'


# カメラの起動
cap = cv2.VideoCapture(0)

while(True):

    # 動画ストリームからフレームを取得
    ret, frame = cap.read()

    local_image = 

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type': 'application/octet-stream'
    }
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
        'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
    }
    data = open(local_image, "rb")
    response = requests.post(face_api_url, params=params, headers=headers, data=data)
    faces = response.json()
    print(faces)


    image = Image.open(local_image);
    plt.figure(figsize=(8, 8))
    ax = plt.imshow(image, alpha=0.6)
    for face in faces:
        fr = face["faceRectangle"]
        fa = face["faceAttributes"]
        origin = (fr["left"], fr["top"])
        p = patches.Rectangle(
            origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b')
        ax.axes.add_patch(p)
        plt.text(origin[0], origin[1], "%d, %d"%(int(fa["emotion"]["disgust"]*100), fa["age"]),
                 fontsize=20, weight="bold", va="bottom")
    _ = plt.axis("off")
    plt.show()



cap.release()
cv2.destroyAllWindows()
