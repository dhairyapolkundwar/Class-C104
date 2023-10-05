import cv2
# For Reading Image
img = cv2.imread("assets/butterfly.jpg")

# For Displaying Image
cv2.imshow("Display Image", img)

# Convert Image To Grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Displaying Grayscale Image
cv2.imshow("Grayscale Image", gray_img)

# Printing Image
cv2.waitKey(0)
