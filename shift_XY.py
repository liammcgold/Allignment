import numpy as np
import padded_shift as ps

def shift(array,x_dir,x_shift,y_dir,y_shift):
    arr=array

    if x_dir == "L":
        arr = np.roll(arr, -x_shift)

    if x_dir == "R":
        arr = np.roll(arr, x_shift)

    arr=np.transpose(arr)

    if y_dir == "U":
        arr = np.roll(arr, -y_shift)

    if y_dir == "D":
        arr = np.roll(arr, y_shift)

    arr=np.transpose(arr)


    return arr