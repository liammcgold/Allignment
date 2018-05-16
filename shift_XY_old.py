import numpy as np
import padded_shift_old as ps

def shift(array,x_dir,x_shift,y_dir,y_shift):
    arr=array
    arr=ps.shift(arr,x_dir,x_shift)
    if(y_dir=="U"):
        y_dir="L"
    else:
        y_dir="R"
    arr=np.transpose(arr)
    arr=ps.shift(arr,y_dir,y_shift)
    arr=np.transpose(arr)
    return arr