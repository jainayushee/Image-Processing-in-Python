import matplotlib.image as matplotimg
import matplotlib.pyplot as plot
from PIL import Image 
# importing OpenCV library
import cv2

### Loading an image to matplotlib module
image = matplotimg.imread('ImageProcessing\sample_image.jpg')

#Check characteristics of the image
print(type(image))
print(image.shape)
print(image)

#Plot and show image using matplotlib
image_plot = plot.imshow(image)
plot.show()

### Resizing image using Pillow lib
image_new = Image.open('ImageProcessing\sample_image.jpg')

resized_image = image_new.resize((200, 200))
resized_image.save('sample_image_resized.jpg')

result = matplotimg.imread('ImageProcessing\sample_image_resized.jpg')
result_plot = plot.imshow(result)
plot.show()

### Graying image using OpenCV
image_new_cv = cv2.imread('ImageProcessing\sample_image.jpg')

grayscale_image = cv2.cvtColor(image_new_cv, cv2.COLOR_RGB2GRAY)
cv2.imshow('image', grayscale_image)
cv2.imwrite('sample_grayscale_image.jpg', grayscale_image)