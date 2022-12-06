
from PIL import Image
import pickle


def DisplayImage(image):
  #read the image
  #im = Image.open("D:/Documents/GitHub/noTABene/Scripts/test_img.png")
  #show image
  image.show()

def UnPackData(data):
  return pickle.dumps(data)

def PackData(data):
  return pickle.loads(data)