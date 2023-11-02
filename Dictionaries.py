from Basketball_data import Games, Sdict, Pdict

print(Games)
#return first row
Games[0]

#list = ordered set of elements, referenced by element position
#dictionary is not ordered, referenced by key
dict1 = {'key1':'val1','key2':'val2','key3':'val3' }

print(dict1['key1'])
#= val1

#players dictionary
print(Pdict['KobeBryant'])
#returns number 0, which is row in which the player lies

print(Games[Pdict['DerrickRose']])
#points derrick rose scored every year

print(Games[Pdict['DerrickRose']])[Sdict['2012']]
#points derrick rose scored in 2012