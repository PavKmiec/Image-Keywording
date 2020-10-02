# IPTC-Keywording
IPTC Image Keywording script

Python script for adding keywords to image meta-data.
This script uses Clarifai API to generate keywords based on their pre-trained image recognition models.

The overall goal of this script (and maybe an app in the future) is to help automate image workflow preparation
(keyword/tag generation) for stock photography libraries such as Alamy which require tags/keywords that describe images.

This script saves generated keywords to image metadata which are recognised
by stock photography libraries and are imported automatically
(saving us time by not having to enter keywords manually). 

To get started you need:

1. Clone the repo

2. Clarifai account at: clarifai.com (it's free), once registered, create an app and generate API key
 - create new file "cred.py" in the app root directory and insert this line into that file:
    key="YOUR API KEY HERE"
 - save the file

3. Install Libraries:
 - pip3 install clarifai
 - pip3 install iptcinfo3
 - pip3 install pillow
 
 
 have fun...
