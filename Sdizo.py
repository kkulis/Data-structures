import random 
#creating txt file
f=open("baza.txt","w+")

#adding numbers to file

for i in range(10):
    x=random.randint(1,101)
    f.write("%d\r\n" % x)