import cv2

image = cv2.imread("images.jpg") 

def clipping(intensitas):
    for x in range (len(image)):
        for y in range (len(image[0])):
            if intensitas < 0:
                return 0
            if intensitas > 255:
                return 255
            return intensitas