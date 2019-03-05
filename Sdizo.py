import random
import time
from config import *

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

#adding numbers to file and into list
base_array=[]

for i in range(number_of_numbers):
    x=random.randint(1,range_of_numbers)
    base_array.append(x)
    f.write("%d\r\n" % x)

#closing file
f.close()

##print(base_array)

#quicksorting, measuring time and appending result to file
f_out=open("quicksorted.txt", "w+")
q_start = time. time()
for i in range(number_of_iterations):
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
for i in range(number_of_iterations):
    bsorted_array=bubble_sort(base_array)
b_end=time. time()
b_time=b_end-b_start
print("bubblesort time: %f" %b_time)
for item in bsorted_array:
    f_outb.write("%d\r\n" % item)
##print(bsorted_array)
f_outb.close()