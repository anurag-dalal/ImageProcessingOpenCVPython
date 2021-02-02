# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

# decompose image img in n images
def imageRandomPartition(img, n):
    # enc will store n images
    enc = []
    # initialize enc with zeros of shape img
    for i in range(n):
        enc.append(np.zeros(img.shape))
    # loops over all rows of img
    for i in range(img.shape[0]):
        # loops over all columns of img
        for j in range(img.shape[1]):
            # get a random number between 0 and n
            r = np.random.randint(n)
            # get the pixel i,j from image and save it to nth enc
            enc[r][i,j] = img[i,j]
    # return enc
    return enc

def imageReconstructionFromPartition(img):
    # initialize reconstructed image with zeros
    im = np.zeros(img[0].shape)
    # sum all the img in im
    for i in range(len(img)):
        im = im + img[i]
    # set pixel value higher than 255 to 255
    im[im > 255] = 255
    # return im as unit8 type
    return im.astype('uint8')

#  for splitting into 20 images
n = 20
I = cv2.imread('Lenna.png')
I = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
cv2.imwrite('Lenna_gray.png', I) 
plt.imshow(I, cmap='gray')
plt.title("Original Image") 
plt.xticks([])
plt.yticks([])
enc = imageRandomPartition(I, n)
plt.show()
for i in range(n):
    plt.subplot(5,4,i+1)
    plt.imshow(enc[4], cmap='gray', vmin=0, vmax=255)
    plt.xticks([])
    plt.yticks([])
    cv2.imwrite('Lenna_enc_'+str(i)+'.png', enc[i])
plt.show()

I2 = imageReconstructionFromPartition(enc)
plt.show()
plt.imshow(I2, cmap='gray')
plt.title("Decrpyted Image") 
plt.xticks([])
plt.yticks([])
plt.show()
cv2.imwrite('Lenna_decr.png', I2) 