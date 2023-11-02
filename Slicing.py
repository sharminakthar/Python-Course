#taking a subset of a list

# 0   1   2   3   4   5   6   7   8   9   
#'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J'

# 2:7
# refers to
# 2   3   4   5   6   
#'C' 'D' 'E' 'F' 'G'

#negative indexation
#'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J'
#-10 -9  -8  -7  -6  -5  -4  -3  -2  -1 
# -8:-3
#returns the same

#Advanced Slicing
#Start:Finish:Step

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G' ,'H' ,'I' ,'J' ]
print(letters)

#big slice
print(letters[:])

#same
print(letters[2:7])
print(letters[-8:7])
print(letters[-8:-3])

#advanced slicing
print(letters[2:9:2])

#whole list in steps of 3
print(letters[::3])

#negative step reverses list