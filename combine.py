import os
from clarifai.rest import ClarifaiApp
from PIL import Image
import glob
from iptcinfo3 import IPTCInfo

# instance of Clarifai App - passing in api key
app = ClarifaiApp(api_key='8347755eb1694ac8a447cdec8261a9db')
# selection of pre-trained model (for image recognition)
model = app.public_models.general_model

# folder containing multiple image files
fileFolder = glob.glob('./images/*.jpg')


# dictionary to keep file path and keywords
data = {}

def createDict():
    for item in fileFolder:
        new_data = {item: []}
        data[item] = new_data[item]

createDict()

# for key, value in data.items():
#     print(key, value)
def resize(photo):
        basewidth = 300
        img = Image.open(photo)
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        #img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        out = img.resize((basewidth,hsize), Image.ANTIALIAS)
        out.save()
        return img.filename # TODO return image path instaed of image !!

print('---------------------------------------------')


# loop data dictionary 
for key, value in data.items():
        print(key)
        response = model.predict_by_filename(key) # get image path from resize method TODO
        for r in response['outputs'][0]['data']['concepts']:
                data[key].append(r['name'])
                print(r['name']) # for each element in response print key-words



# take the values in dict, match key value to a file path and append IPTC keywords to file
for key, value in data.items():
        #print(os.path.basename(key))
         info = IPTCInfo(key)
         for item in value:
                 newValue = item
                 info['keywords'].append(newValue)
         info.save()
