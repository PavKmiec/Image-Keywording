import os
from clarifai.rest import ClarifaiApp
from PIL import Image
import glob
from iptcinfo3 import IPTCInfo
# instance of Clarifai App - passing in api key
app = ClarifaiApp(api_key='KEY HERE')
# selection of pre-trained model (for image recognition)
model = app.public_models.general_model

# list vaiable for storing image locations
image_list = []


# folder containing multiple image files
fileFolder = glob.glob('./street/*.*')



data = {}

def createDict():
    for item in fileFolder:
        new_data = {item: []}
        data[item] = new_data[item]

createDict()


for key, value in data.items():
    print(key, value)


print('---------------------------------------------')



for key, value in data.items():
        print(key)
        response = model.predict_by_filename(key)
        for r in response['outputs'][0]['data']['concepts']:
                data[key].append(r['name'])
                print(r['name']) # for each element in response print key-words


# check data dict
for key, value in data.items():
    print(key, value)
