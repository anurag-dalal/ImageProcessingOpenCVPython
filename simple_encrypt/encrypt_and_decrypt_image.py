# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2

def encrypt(img):
    key = np.random.randint(0,255,img.shape)
    for i in range(img.shape[0]):
        # loops over all columns of img
        for j in range(img.shape[1]):
            img[i,j] = img[i,j]^key[i,j]
    return img,key

def decrypt(img, key):
    for i in range(img.shape[0]):
        # loops over all columns of img
        for j in range(img.shape[1]):
            img[i,j] = img[i,j]^key[i,j]
    return img

I = cv2.imread('cameraman.tif')
I = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
cv2.imwrite('Lenna_gray.png', I) 
plt.subplot(2,2,1)
plt.imshow(I, cmap='gray')
plt.title("Original Image") 
plt.xticks([])
plt.yticks([])

enc, key = encrypt(I)
plt.subplot(2,2,2)
plt.imshow(enc, cmap='gray')
plt.title("Encrypted image") 
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(key, cmap='gray')
plt.title("Key") 
plt.xticks([])
plt.yticks([])

dec = decrypt(enc, key)
plt.subplot(2,2,4)
plt.imshow(dec, cmap='gray')
plt.title("Decrypted") 
plt.xticks([])
plt.yticks([])