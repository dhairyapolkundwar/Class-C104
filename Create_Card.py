import cv2

img = cv2.imread("assets/poster.jpg")
rocket = img[120:360, 400:500]
text_to_show = "I Love Coding"
cv2.putText(img, text_to_show, (20, 20), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0,0,255))
cv2.imshow("Output", rocket)
cv2.imshow("Original Output", img)
cv2.waitKey(0)