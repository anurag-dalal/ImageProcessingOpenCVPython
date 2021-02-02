# ImageProcessingOpenCVPython
Some simple implementation using OpenCV in python

# 1. kMeans clustering of colors in an image
[k-means wiki](https://en.wikipedia.org/wiki/K-means_clustering)
[k-means pyimagesearch](https://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/)

The input image used is: \
![Lenna Image](/kmeans/Lenna.png "Input image")

The output is: \
![kmean Image](/kmeans/kmean.png "Output Image")

To achieve this the scikit-learn library is used
Five clusters are used and so we find how much percent of color are there in the 5 most used colors in the bar. \

# 2. Splitting or decomposing image
An image(grayscale) is splitted into n number of images by iterating over the rows and columns of the original image and randomly copying the pixel value to any of the n images.\

# 3. Simple encryption of image using XOR
![Output Image](/simple_encrypt/Figure2021-02-02151720.png "Output Image")
