from PIL import Image
from os import listdir, mkdir
from os.path import isfile, join
import re

src_path = "./src/"
out_path = "./out/"

onlyfiles = [f for f in listdir(src_path) if isfile(join(src_path, f))]

def modify_line(data):
    out = []
    for i in range(576):
        out.extend(data[i*832:i*832+720])

    return bytes(out)

for file_ in onlyfiles:
    imgSize = (720, 576)
    f = open(src_path+file_, 'rb')
    rawData = f.read()
    rawData = modify_line(rawData)
    image = Image.frombytes('L', imgSize, rawData, 'raw')
    try:
        mkdir(out_path)
    except:
        pass
    image.convert('L').save(out_path+"out_"+file_+".bmp")


