import numpy as np
#list
l = [1, 5 , -4, -20]
#array
a = np.array(l)

#in arrays you cant have different data types
b = np.array([12, 45, 63.3, True, 'abc'])
print(b)
#['12' '45' '63.3' 'True' 'abc']

#Slicing arrays
c = a[2:4]
#doesnt create new array but works with original array
c [:] = 11

#to create copy of array
d= a.copy()