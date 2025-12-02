import cv2
import numpy as np

img = cv2.imread('/Users/gamogh/Desktop/personal/webpage/amogh112.github.io/images/multitask.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cols = np.where(gray.mean(axis=0) > 250)[0]
splits = np.split(cols, np.where(np.diff(cols) > 1)[0] + 1)
gaps = [s[0] for s in splits if len(s) > 10]

parts = []
start = 0
for gap in gaps:
    parts.append(img[:, start:gap])
    start = gap
parts.append(img[:, start:])

stacked = np.vstack(parts)
cv2.imwrite('/Users/gamogh/Desktop/personal/webpage/amogh112.github.io/try/multitask_stacked.png', stacked)
