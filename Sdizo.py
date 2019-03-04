import random

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

#creating txt file
f=open("baza.txt","w+")

#adding numbers to file and into list
base_array=[]

for i in range(10):
    x=random.randint(1,101)
    base_array.append(x)
    f.write("%d\r\n" % x)

#closing file
f.close()

print(base_array)

#quicksorting and appending result to file
f_out=open("quicksorted.txt", "w+")
sorted_array=quick_sort(base_array)
for item in sorted_array:
    f_out.write("%d\r\n" % item)
print(sorted_array)