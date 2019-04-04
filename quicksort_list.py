import random
import time
import math
from config import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticks


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
f_times=open('q_times.txt', "w+")
#f_outb=open("bubblesorted.txt", "w+")

#creating arrays
base_array=[]
q_times_array=[]
av_array=[]
q_whole_start=time. time()

#generating numbers, quicksorting, time measuring, appending 
for i in range(0,number_of_numbers):
    x=random.randint(1,range_of_numbers)
    base_array.append(x)
    f.write("%d\r\n" % x)
    for j in range(100):
        q_start=time. time()
        sorted_array=quick_sort(base_array)
        q_end=time. time()
        q_time=q_end-q_start
        av_array.append(q_time)
        if(i==number_of_numbers-1 and j==99):
            for item in sorted_array:
                f_out.write("%d\r\n" %item)
    av_time=sum(av_array)/len(av_array)
    del av_array[:]
    q_times_array.append("%f" %av_time)
    f_times.write("%f \r\n" %av_time)
    #if i == number_of_numbers-1:
        #for item in sorted_array:
            #f_out.write("%d\r\n" % item)
#print(q_times_array)
#print(av_array)
q_whole_end=time. time()
q_whole=q_whole_end-q_whole_start
print(q_whole)
f_out.close()
f.close()
f_times.close()

#nlog(n)
log_array=[]
for n in range(1,number_of_numbers):
    y=n*math.log10(n)/4
    log_array.append(y)
#appending first element to array (0log(0))
log_array.insert(0,0)
#print(log_array)

#n_array=[]
#for n in range(1,number_of_numbers):
    #y=n**2
    #n_array.append(y)
#appending first element to array (0log(0))
#log_array.insert(0,0)
#print(n_array)

#plotting
fig=plt.figure()
ax=fig.add_subplot(111)
plt.yticks(np.arange(0,0.002))
plt.title("quicksort (list)")
plt.xlabel("number of operations")
plt.ylabel("time(s)")
plt.plot(q_times_array, 'bo', label='time')
plt.plot(log_array, 'r', label='n(logn)')
plt.legend(loc='upper left')
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