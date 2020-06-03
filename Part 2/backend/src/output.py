#required imports
import matplotlib
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import image as mpimg
from matplotlib.pyplot import figure
from cv2 import cv2
import numpy as np


def cartoonifier(imagepath):

    #TO DO
    #step 1
    #Use bilateral filter for edge-aware smoothing.


    num_down = 1 # number of downsampling steps 
    num_bilateral = 4 # number of bilateral filtering steps

    img = cv2.imread(imagepath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # downsample image using Gaussian pyramid(see opencv 'pyrDown()' function)
    for i in range (num_down):
        img = cv2.pyrDown(img)

    # repeatedly apply small bilateral filter instead of
    # applying one large filter
    for i in range (num_bilateral):
        img = cv2.bilateralFilter(img, 15, 75, 75)

    # upsample image to original size (see opencv 'pyrUp()' function)
    for i in range (num_down):
        bilateralImg = cv2.pyrUp(img)

    #plt.imshow(bilateralImg)


    # ## Step#2
    # ### In this step we will blur the original image. This is considered as a pre-processing step before we move on towards the edge detection step. We will apply a median filter on the image, which replaces each pixel value with the median value of all the pixels in a small neighborhood.

    # In[5]:


    #TO DO
    #step 2
    # convert to grayscale and apply median blur
    img = cv2.imread(imagepath)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    medianBlurImg = cv2.medianBlur(grayImg, 5)

    #plt.imshow(medianBlurImg, cmap = 'gray')


    # ## Step#3
    # 
    # ### In this step we will create an edge mask from the output produced in step#2 using adaptive thresholding 

    # In[14]:


    #TO DO
    #step 3
    # detect and enhance edges(see opencv 'adaptiveThreshold()' function)
    edgeMask = cv2.adaptiveThreshold(medianBlurImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2,)
    #plt.imshow(edgeMask, cmap = 'gray')


    # ## Final Step
    # 
    # ### In this step we will combine the output produced in step#1 and step#3 using a bitwise and operator to produce our final output.(Note: You need to convert output from step#3 to color first)

    # In[40]:


    #TO DO
    #Final Step
    # convert back to color, bit-AND with color image
    finalMask = cv2.cvtColor(edgeMask, cv2.COLOR_GRAY2RGB) 

    (x1, y1, z1) = bilateralImg.shape
    (x2, y2, z2) = finalMask.shape


    if x1 > x2:
        bilateralImg = np.delete(bilateralImg, x1 - 1, 0)
    elif x2 > x1:
        finalMask = np.delete(finalMask, x2 - 1, 0)
        
    if y1 > y2:
        bilateralImg = np.delete(bilateralImg, y1 - 1, 1)
    elif y2 > y1:
        finalMask = np.delete(finalMask, y2 - 1, 1)

    finalImg = cv2.bitwise_and(bilateralImg, finalMask, mask = None)

    return finalImg

    # In[ ]:




