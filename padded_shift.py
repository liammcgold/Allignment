import numpy as np
'''
only works if padding on side to be shifted is greater than shift number
'''

def shift(array,dir, shift):

    arr=array

    if(arr.ndim>2):
        print("too many dims in input array")
        return

    if dir == "L":
        arr = np.roll(arr, -shift)

    if dir == "R":
        arr = np.roll(arr, shift)

    return arr

