import numpy as np
'''
only works if padding on side to be shifted is greater than shift number
'''

def shift(array,dir, shift):

    arr=array

    if(arr.ndim>2):
        print("too many dims in input array")
        return

    if (arr.ndim>1):
        rows=arr.shape[0]
    else:
        rows=1



    if(rows>1):
            for m in range(0,rows):
                #shift from nth (shift number) term to end left by shift amount
                for n in range(shift-1, arr.shape[1]-1):
                    arr[m, n-shift]=arr[m, n]

                #pad with last number
                pad=arr[m,-1]

                #from shifted end to actual end pad
                for n in range(arr.shape[1]-shift-1, arr.shape[1]-1):
                    arr[m, n]=pad




            for m in range(0, rows):

                new_arr = np.zeros(arr.shape[1])

                # shift from nth (shift number) term  from end to beginning right by shift amount
                for n in range(0, arr.shape[1] - shift ):
                    new_arr[n+shift] = arr[m, n]

                #pad with first number
                pad = arr[m, 0]

                # from shifted end to actual end pad
                for n in range(0, shift):
                    new_arr[ n] = pad

                arr[m]=new_arr



    else:
        if dir == "L":
            # shift from nth (shift number) term to end left by shift amount
            for n in range(shift - 1, arr.shape[0] - 1):
                arr[n - shift] = arr[ n]

            # pad with last number
            pad = arr[ -1]

            # from shifted end to actual end pad
            for n in range(arr.shape[0] - shift - 1, arr.shape[0] - 1):
                arr[ n] = pad
        if dir == "R":
            new_arr=np.zeros(arr.shape[0])
            # shift from nth (shift number) term  from end to beginning right by shift amount
            for n in range(0, arr.shape[0] - shift ):
                new_arr[ n + shift] = arr[ n]

            # pad with first number
            pad = arr[ 0]

            # from shifted end to actual end pad
            for n in range(0, shift ):
                new_arr[ n] = pad
            arr=new_arr
    return arr




