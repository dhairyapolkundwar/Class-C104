import cv2
import numpy as np

black = np.zeros([600, 600])
#print(black)
#f_row = black[:, 1:2]
#print(f_row)

black[200:400, 200:400] = 255
print(black)
cv2.imshow("Black Image", black)
cv2.waitKey(0)