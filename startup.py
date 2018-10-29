x=['shubham',65,2.5]
for i in range(12,20,1):
    if i%5 == 0:
        print (i)

for i in range(1,10,1):
    if i%3==0 or i%5==0:
        continue
    else:
        print (i)

        
import array as arr
vals = arr.array('i',[5,9,4,5,6,8,1])
for i in range(len(vals)):
    print (vals[i])
for e in vals:
print(e)

import array as arr
from array import *
ar1 = arr.array('i',[])
n = int(input("Pleas enter the length of Array : "))
for i in range(n):
    i=int(input("Enter the element : "))
    ar1.append(i)
