import cv2

img = cv2.imread('input/p0-1-0.png',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
