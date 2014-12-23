# This program sorts an array
# Written by the collective minds of http://squarific.com/DemocraticProgramming/
# License: MIT, although WTFPL is cooler
unsorted_array = [98, 23, -1, 48, 109, 20]
def sort_array (array):
    array = array[:] # Copies the array
    for a in range(len(array) - 1, 0, -1):
        for b in range(a):
            if array[b] > array[b + 1]:
                array[b], array[b + 1] = array[b + 1], array[b]
    return array
sorted_array = sort_array(unsorted_array)