#!/usr/bin/env python
import cv2
import numpy as np

img = cv2.imread('./image/Space.jpg')
cv2.imwrite('tand.png',img)
