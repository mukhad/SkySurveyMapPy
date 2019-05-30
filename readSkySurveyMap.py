import numpy as np
import os

import drawSkySurveyMap
import drawTTPlot

fmhz = "25"
fmhz2 = "16.7"

freq = {"25": 2, "20": 3, "16.7": 4, "14.7": 5, "12": 6, "10": 7}
n = 51 * 48

ra = np.ndarray(n, dtype=np.float32)  # list()  # 0
dec = np.ndarray(n, dtype=np.float32)  # list()  # 1
t = np.ndarray(n, dtype=np.float32)  # list()
t2 = np.ndarray(n, dtype=np.float32)  # list()

file_name = "data/s56ellips_SS5019_data09-04-2012.txt"

#file_name = "data/urans56ellips_SS5019_data09-04-2012_1.txt"

#file_name = "tmp/exmpl.txt"

desc = os.path.basename(file_name)


i = 0
with open(file_name) as f:
    for line in f:
        s = line.split()

        try:
            ra[i] = float(s[0])
            dec[i] = float(s[1])
            t[i] = float(s[freq[fmhz]])
            t2[i] = float(s[freq[fmhz2]])
            i += 1
        except (IndexError, ValueError):
            print(s)

print("len: {0}".format(len(t)))
print(ra[0:10])
print(dec[0:10])
print(t[0:10])


#drawSkySurveyMap.scatter_map(ra,dec,t,fmhz)
#print("scatter")

#drawSkySurveyMap.contour_map(ra,dec,t,fmhz)
#print("contour")

drawSkySurveyMap.imshow_map(ra,dec,t,fmhz,desc)
print("imshow")

drawTTPlot.tt_plot(t,t2,fmhz,fmhz2,desc)
print("tt plot")



