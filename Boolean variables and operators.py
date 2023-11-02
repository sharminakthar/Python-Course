#Boolean / logical:
#True
#false

#print (expression) returns boolean
print (4<5)
print (10>100)
print (4==5)

# Check if two values equal: == 
# Not equal: ! = ,. 
# Greater than: <
# Less than: >
# Greater than or equal to: <= 
# Less than or equal to: >=
# Bitwise operation
# Conjuction: and 
# Disjunction: or
# Negation: not

result = 4 < 5 
print(result)
print(type(result))
#True

result2 = not ( 5 > 1 )
print(result2)
print(type(result2))
#False

result3 = result or result2
print((result3))
print(type(result3))

result4 = result and result2
print((result4))
print(type(result4))