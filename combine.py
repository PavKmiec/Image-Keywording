import os
from clarifai.rest import ClarifaiApp
from PIL import Image
import glob
from iptcinfo3 import IPTCInfo
import cred

# instance of Clarifai App - passing in api key
app = ClarifaiApp(api_key=cred.key)
# selection of pre-trained model (for image recognition)
model = app.public_models.general_model

# folder containing multiple image files
fileFolder = glob.glob('/home/px/Desktop/repos/keywording/IPTC-Keywording/images/*.jpg')


# dictionary to keep file path and keywords
data = {}

# create dictionary for storing file path as key and array of keywords as value 
def createDict():
    for item in fileFolder:
        new_data = {item: []}
        data[item] = new_data[item]

createDict()

print('---------------------------------------------')



# loop data dictionary
#  
for key, value in data.items():
        print(key)
        print(value)

        # set recognition model
        response = model.predict_by_filename(key) # TODO get image path from resize method TODO

        # append generated keywords in dictionary
        for r in response['outputs'][0]['data']['concepts']:
                data[key].append(r['name'])
                print(r['name']) # for each element in response print key-words



# take the values from dictionary, 
# match key value to a file path and append IPTC keywords to image file
for key, value in data.items():
        #print(os.path.basename(key))
         info = IPTCInfo(key)
         for item in value:
                 newValue = item
                 info['keywords'].append(newValue)
         info.save()

#--------------------------------------------------------------------#

## TODO

## Implement image resizing method to improve performance
###  Keywords MUST be saved back to Oryginal (not resized images)

# # method to resize
# def resize(photo):
#         basewidth = 300
#         img = Image.open(photo)
#         wpercent = (basewidth/float(img.size[0]))
#         hsize = int((float(img.size[1])*float(wpercent)))
#         #img = img.resize((basewidth,hsize), Image.ANTIALIAS)
#         out = img.resize((basewidth,hsize), Image.ANTIALIAS)
#         out.save()
#         return img.filename # TODO return image path instaed of image !!
