import numpy as np
import padded_shift as ps
import shift_XY as sh


array = np.array([[.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1],
                  [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1],
                  [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1],
                  [.1, .1, .1, .1, .1, 4, 5, 6, 7, 8, 9, .1, .1, .1, .1, .1],
                  [.1, .1, .1, .1, .1, 4, 5, 6, 7, 8, 9, .1, .1, .1, .1, .1],
                  [.1, .1, .1, .1, .1, 4, 5, 6, 7, 8, 9, .1, .1, .1, .1, .1],
                  [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1],
                  [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1],
                  [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1]]
                 )
array = sh.shift(array, "R", 3, "U", 1)

target_array = np.array([[.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1],
                         [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1],
                         [.1, .1, .1, .1, .1, .1, .1, .1, 4, 5, 6, 7, 8, 9, .1, .1],
                         [.1, .1, .1, .1, .1, .1, .1, .1, 4, 5, 6, 7, 8, 9, .1, .1],
                         [.1, .1, .1, .1, .1, .1, .1, .1, 4, 5, 6, 7, 8, 9, .1, .1],
                         [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1],
                         [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1],
                         [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1],
                         [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1]])


if((array==target_array).all):
    print("VALID")