import random 
#creating txt file
f=open("baza.txt","w+")

#adding numbers to file and into list
base_array=[]

for i in range(10):
    x=random.randint(1,101)
    base_array.append(x)
    f.write("%d\r\n" % x)

print(base_array)
