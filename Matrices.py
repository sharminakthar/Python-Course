# A matrix in python is row by column
# A[2,3] is the fourth column, third row

#Indexing 
#         [:,0]         [:,1]           [:,2]             [:,3]  
#         1st column    2nd column ....
# [0,:] --> top row
# [1,:] --> middle row
# [2,:] --> last row

# Building a matrix

# populated row by row
# np.reshape(*,*,'C')

# populated column by column 
# np.reshape(*,*,'C')

# puts rows into matrix, combines data elements into matrix
# np.array()

import numpy as np
mydata = np.arange(0,20)
print(mydata)
#[0,1,....19]

#five rows by four columns
matrix_1 = np.reshape(mydata, (5,4), order = 'C')
print(matrix_1)

#same data populated in different way
matrix_2 = np.reshape(mydata, (5,4), order = 'F')
print(matrix_2)

#how to get number 10 in the matrix
element = matrix_1[2,2]
#print(element)
element2 = matrix_2[0,2]

#object oriented programming OOP concept
#type(mydata) = array
#therefore mydata is an object

#np.reshape(mydata) =  print(mydata.reshape(5,4))

r1 = ['i', 'am', 'happy']
r2 = ['what', 'a', 'day']
r3 = [1, 2, 3]

#lists of lists
combined = [r1, r2, r3]
print(combined)
#gives an array, combined

#turn lists of lists into matrix 
combined_matrix = np.array([r1, r2, r3])
print(combined_matrix)
#matrix of strings