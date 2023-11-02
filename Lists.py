Myfirstlist = [3, 45, 56, 732]
print(Myfirstlist)
print(type(Myfirstlist))

#mixed data types
Mysecondlist = ['hello', 5 , True, -100]
print(type(Mysecondlist))

#list inside list
Mythirdlist = [1, False, Myfirstlist]

#range(15) = range(0,15)
#list(range(15)) = [0, 1, 2 ... .14]

y = list(range(8))
#[0, 1, 2 ... 7]

z = list(range(100,121))
#[100, 101, ... 120]

w = list(range(100,111,2))
#[100, 102, 104, 106, 108, 110]

u = ['a', 'b', 'c', 'd', 'e']
print(u [0])
#gives first element / 0th cell

#length of a string
print(len(u))

# indexation:
# 0 ---- 1 ---- 2 ---- 3 ---- 4
# negative indexation
# -5 --- -4 --- -3 --- -2 --- -1 

print(u[-1])

#overwrite values
u[2] = 63
print(u)
