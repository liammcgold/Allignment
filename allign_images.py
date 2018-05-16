import numpy as np
import shift_XY as sh
import matplotlib.pyplot as plt
from PIL import Image
import os
from shutil import copyfile
import time

target_dir = "/media/curie/MOUSELIGHT/VCN_bin2_tiffs"

tifs = []
for root, dirs, files in os.walk(r'/media/curie/MOUSELIGHT/VCN_bin2_tiffs'):
    for file in files:
        if file.endswith('.tif'):
              tifs.append(file)

#sort in case of issues
tifs.sort()




for n in range(1154,len(tifs)):
    if(n>1154):
       print("shifting...",tifs[n])
       time_start=time.time()
       im = Image.open("/media/curie/MOUSELIGHT/VCN_bin2_tiffs/"+tifs[n])
       im= np.asarray(im)
       im = sh.shift(im,"L",98,"D",94)
       im=Image.fromarray(im)
       im.save("/media/curie/MOUSELIGHT/VCN_bin2_tiffs_shifted/"+tifs[n],)
       time_run = time.time()-time_start
       print("shifted in: ",int(time_run)," seconds")

    else:
        copyfile("/media/curie/MOUSELIGHT/VCN_bin2_tiffs/"+tifs[n],"/media/curie/MOUSELIGHT/VCN_bin2_tiffs_shifted/"+tifs[n])
