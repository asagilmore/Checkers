from PIL import Image
import numpy as np

rangeNumber = 52
for i in range(rangeNumber):
    im = Image.open('moderateDem'+str(i)+'.jpg', 'r')
    pix_val = list(im.getdata())
    pix_val_float = []
    for q in range(len(pix_val)):
        pix_val_float.append(pix_val[q]/255)
    array = np.array(pix_val_float)
    
def imgToArray(filename):
    im = Image.open(filename,'r')
    pix_val = list(im.getdata())
    pix_val_float = []
    for q in range(len(pix_val)):
        pix_val_float.append(pix_val[q]/255)
    array = np.array(pix_val_float)
    return array

def folderToArray(name,len):
    array = []
    for i in range(len):
        array.append(imgToArray(name+str(i)+'.jpg'))
    return array

def convertBack(array):
  array = array * 255
  image = np.array(array)
  image = np.resize(image, (208, 176))
  newnewimage = np.array(image)
  data = Image.fromarray(newnewimage)
  data.show()   