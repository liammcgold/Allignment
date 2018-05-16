import numpy as np
import padded_shift as ps
import padded_shift_old as pso
import shift_XY as sh
import shift_XY_old as sho
import time


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

target_array = np.array([[.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1],
                          [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1],
                          [.1, .1, .1, .1, .1, .1, .1, .1, 4, 5, 6, 7, 8, 9, .1, .1],
                          [.1, .1, .1, .1, .1, .1, .1, .1, 4, 5, 6, 7, 8, 9, .1, .1],
                          [.1, .1, .1, .1, .1, .1, .1, .1, 4, 5, 6, 7, 8, 9, .1, .1],
                          [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1],
                          [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1],
                          [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1],
                          [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1]])

percent_improvement=[0]*10000
t_new_arr=[0]*10000
t_old_arr=[0]*10000
for n in range(0,10000):
    #get old runtime
    t_start_old=time.time()
    array_old = sho.shift(array, "R", 3, "U", 1)
    t_old=time.time()-t_start_old

    t_old_arr[n]=t_old

    #get new runtime

    t_start_new=time.time()
    array_new = sh.shift(array, "R", 3, "U", 1)
    t_new=time.time()-t_start_new

    t_new_arr[n]=t_new


t_new_avrg=np.average(t_new_arr)
t_old_avrg=np.average(t_old_arr)
percent_improvement_avrg=(100*(t_old_avrg-t_new_avrg)/t_old_avrg)




if((array_new==target_array).all()):
    print("-correct output-")
    print("improvement in runtime:",percent_improvement_avrg,"%")
else:
    print("does not match")
