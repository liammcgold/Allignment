import numpy as np
import shift_XY as sh
import matplotlib.pyplot as plt
import os
from shutil import copyfile

target_dir = "/media/curie/MOUSELIGHT/VCN_bin2_tiffs"

tifs = []
for root, dirs, files in os.walk(r'/media/curie/MOUSELIGHT/VCN_bin2_tiffs'):
    for file in files:
        if file.endswith('.tif'):
              tifs.append(file)

#sort in case of issues
tifs.sort()




for n in range(1100,len(tifs)):
    if(n>1154):
       print("shift")
       im = plt.imread("/media/curie/MOUSELIGHT/VCN_bin2_tiffs/"+tifs[n])
       im = sh.shift(im,"L",98,"D",94)
       plt.imsave("/media/curie/MOUSELIGHT/VCN_bin2_tiffs_shifted/"+tifs[n]+tifs[n],im)

    else:
        copyfile("/media/curie/MOUSELIGHT/VCN_bin2_tiffs/"+tifs[n],"/media/curie/MOUSELIGHT/VCN_bin2_tiffs_shifted/"+tifs[n])
