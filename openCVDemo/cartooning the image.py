
# Python code to read image
import cv2
 
# To read image from disk, we use
# cv2.imread function, in below method,
#change second argument to zero , making it read grayscale
img = cv2.imread("spong.jpg", 0)

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 
img_blur = cv2.medianBlur(img_gray, 3) 
 
# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array
cv2.imshow("Sponge and Patrick", img_blur)
 
# To hold the window on screen, we use cv2.waitKey method
# Once it detected the close input, it will release the control
# To the next line
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will
# hold the screen until user close it.
cv2.waitKey(0)
 
# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()
