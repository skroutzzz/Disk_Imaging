import os
from pymongo import MongoClient
import gridfs

client = MongoClient('localhost', 27017)
db = client['ImageDatabase']
fs = gridfs.GridFS(db)


img_path = os.path.expanduser('~/Documents/usb.img')

with open(img_path, 'rb') as img_file:
    fs.put(img_file, filename=os.path.basename(img_path))

print("Img uploaded successfully")

