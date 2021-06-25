from datetime import datetime
import numpy as np

ans0 = datetime(2017, 1, 1, 12, 0, 0)
ans1 = datetime(2017, 1, 1, 13, 0, 0)
ans2 = datetime(2017, 1, 1, 14, 0, 0)
ans3 = datetime(2017, 1, 1, 15, 0, 0)

def p(x):
    max_v = - np.infty
    min_v = np.infty
    for i in range(len(X)):
        for j in range(len(X[i])):
            curr = X[i][j]
            if curr < min_v:
                min_v = curr
            if curr > max_v:
                max_v = curr
    return max_v - min_v

ans4 = datetime(2014, 5, 6, 12, 30, 0)

'''
lats = epots.lat
lons = epots.lon
'''