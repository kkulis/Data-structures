import random
import time
from config import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#quicksort function
def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quick_sort(less)+equal+quick_sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array 

#bubblesort function
def bubble_sort(array):

   #Setting the range for comparison (first round: n, second round: n-1  and so on)
   for i in range(len(array)-1,0,-1):

      #Comparing within set range
       for j in range(i):

           #Comparing element with its right side neighbor
           if array[j] > array[j+1]:

               #swapping
               temp = array[j]
               array[j] = array[j+1]
               array[j+1] = temp

   return array


#creating txt file
f=open("baza.txt","w+")
f_out=open("quicksorted.txt", "w+")
#f_outb=open("bubblesorted.txt", "w+")

#creating arrays
base_array=[]
q_times_array=[]

#generating numbers, quicksorting, time measuring, appending 
for i in range(number_of_numbers):
    x=random.randint(1,range_of_numbers)
    base_array.append(x)
    f.write("%d\r\n" % x)
    q_start=time. time()
    sorted_array=quick_sort(base_array)
    q_end=time. time()
    q_time=q_end-q_start
    q_times_array.append("%.3f" %q_time)
    if i == number_of_numbers-1:
        for item in sorted_array:
            f_out.write("%d\r\n" % item)
#print(q_times_array)


#plotting
q_times_array=[x * 10000 for x in q_times_array]
x1=np.arange(0,number_of_numbers,1)
fig, ax = plt.subplots()
ax.scatter(x1,q_times_array)
plt.show()



""" #closing file
f.close()
f_out.close()

##print(base_array)

#quicksorting, measuring time and appending result to file
f_out=open("quicksorted.txt", "w+")
q_start = time. time()
sorted_array=quick_sort(base_array)
q_end = time. time()
q_time=q_end-q_start
print("quicksort time: %f" %q_time)
for item in sorted_array:
    f_out.write("%d\r\n" % item)
##print(sorted_array)
f_out.close()

#bubblesorting, measuring time and appending result to file
f_outb=open("bubblesorted.txt", "w+")
b_start=time. time()
bsorted_array=bubble_sort(base_array)
b_end=time. time()
b_time=b_end-b_start
print("bubblesort time: %f" %b_time)
for item in bsorted_array:
    f_outb.write("%d\r\n" % item)
##print(bsorted_array)
f_outb.close() """