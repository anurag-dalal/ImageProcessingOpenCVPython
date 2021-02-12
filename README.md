# ImageProcessingOpenCVPython
Some simple implementation using OpenCV in python

## Requirements:
```bash
$ pip install numpy
$ pip install matplotlib
$ pip pip install opencv-python
```

# 1. kMeans clustering of colors in an image
[k-means wiki](https://en.wikipedia.org/wiki/K-means_clustering)
[k-means pyimagesearch](https://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/)

The input image used is: \
![Lenna Image](/kmeans/Lenna.png "Input image")

The output is: \
![kmean Image](/kmeans/kmean.png "Output Image")

To achieve this the scikit-learn library is used
Five clusters are used and so we find how much percent of color are there in the 5 most used colors in the bar. 

# 2. Splitting or decomposing image
An image(grayscale) is splitted into n number of images by iterating over the rows and columns of the original image and randomly copying the pixel value to any of the n images.

# 3. Simple encryption of grayscale image using XOR

This example producaes a random key of the same shape as image and XOR it with the input image to encrpyt. \
Then to decrpt the key is XORed with the encrypted image. \
![Output Image](/simple_encrypt/Figure2021-02-02151720.png "Output Image")

# 4. Edge detection using fourier transform
Read [this](https://akshaysin.github.io/fourier_transform.html#.YCYJrWgzY-V) blog for details about using filters in fourier domain in Image Processing.

A high  pass filter is used to detect the edges in an grayscale image.

The output is: \
![Edge Detection Image](/edge_detection_fourier/result.png "Output Image")
