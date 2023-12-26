#!/usr/bin/env python3

import cv2
import numpy as np

image=cv2.imread("/home/ryu/opencv_test/data/moon.jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("moon", image)
print(np.shape(image))
cv2.waitKey(0)
cv2.destroyAllWindows()
