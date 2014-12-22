# This program sorts an array
# Written by the collective minds of http://squarific.com/DemocraticProgramming/
# License: MIT
unsorted_array = [98, 23, -1, 48, 109, 20]
def sort_array (array):
    array = array[:] # Copies the array
    array.sort()
    return array
sorted_array = sort_array(unsorted_array)
print(sorted_array)