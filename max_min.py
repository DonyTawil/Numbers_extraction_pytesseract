import argparse
import imutils
import cv2
import logging, os
import pytesseract
from PIL import Image
import reg_num as reg

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())


# Load the image, convert it to grayscale, blur it slightly,
# and threshold it
image = cv2.imread(args["image"])
image = imutils.resize(image, width=2000)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)                 # When using pytesseract best to only have the grayscale, tried it with threshold and 
                                            # blurr, did not work

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
print(text)
os.remove(filename)

nums = reg.extract_num(text)
nums = sorted(nums)

print("The sorted numbers are ", nums)



