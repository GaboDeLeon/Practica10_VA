import cv2
import numpy as np

img_raw = cv2.imread('imagen_1.jpg')
r = cv2.selectROI(img_raw)
print(r)
roi_cropped = img_raw[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

cv2.imshow("ROI", roi_cropped)
cv2.imwrite("crop.jpeg",roi_cropped)

#///////////////////////////////////////////

gray = cv2.cvtColor(roi_cropped, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
 
height, width = dst.shape
color = (0, 255, 0)

for y in range(0, height):
    for x in range(0, width):
        if dst.item(y, x) > 0.01 * dst.max():
            cv2.circle(roi_cropped, (x, y), 3, color, cv2.FILLED, cv2.LINE_AA)

cv2.imshow('Harris Result', dst)
cv2.imshow('Harris Corner', roi_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
