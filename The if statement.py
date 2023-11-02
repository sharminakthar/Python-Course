import numpy as np
from numpy.random import randn

#---- -2 ---- -1 ---- 0 ---- 1 ---- 2 ----
answer = None
x = randn()
if x > 1:
    answer = 'greater than 1'
else:
    answer = 'less than 1'
print(x)
print(answer)

#[---- -2 ---- [-1] ---- 0 ---- [1] ---- 2 ----]
#Nested statements
answer = None
x = randn()
if x > 1:
    answer = 'greater than 1'
else:
    if x >= -1:
        answer = 'between -1 and 1'
    else:
        answer = 'less than -1'
print(x)
print(answer)

#Chained statements
answer = None
x = randn()
if x > 1:
    answer = 'greater than 1'
elif x >= -1:
    answer = 'between -1 and 1'
else:
    answer = 'less than -1'
print(x)
print(answer)