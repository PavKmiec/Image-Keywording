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

# def loadImages():
#     for filename in fileFolder:
#         im=Image.open(filename)
#         image_list.append(im)
#     return image_list

# loadImages()


for key, value in data.items():
    print(key, value)


print('---------------------------------------------')


# #for each image in list pass in image url with image name to the response 
# for image in image_list:
#     response = model.predict_by_filename(image.filename)
#     print(image)
#     for r in response['outputs'][0]['data']['concepts']: # for each element in response print key-words
#         print(r['name'])


for key, value in data.items():
        print(key)
        response = model.predict_by_filename(key)
        for r in response['outputs'][0]['data']['concepts']:
                data[key].append(r['name'])
                print(r['name']) # for each element in response print key-words



for key, value in data.items():
    print(key, value)

        # new_data = {item: ['']}
        # data[item] = new_data[item]


# import list of year,value pairs

# for year,value in mylist:
#     try:
#         d[year].append(value)
#     except KeyError:
#         d[year] = [value]








        # response = model.predict_by_filename(inageUrl)
        # for r in response['outputs'][0]['data']['concepts']:
        #         print(inageUrl)
        #         print(r['name']) # for each element in response print key-words


