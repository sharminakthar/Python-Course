#increase sample size, answer converges to a value
import numpy as np
from numpy.random import randn

#specify sample size
N = 100

#reset counter
counter = 0 

#iterate over random values
for i in randn(N):
    #check where iterated variable falls
    if (-1 > i and i < 1):
        #increase counter if condition is met
        counter = counter + 1
#calculate hit-ratio
answer = counter / N
#print answer
print(answer)