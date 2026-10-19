set1={1,12,32,24,24,5,2}

print(set1)

print(12 in set1)

set2={}
print(type(set2))

set3=set()
print(type(set3))

set3=set('abcd')
print(set3)

set4=set('acef')
print(set4)

print(set3-set4) #removes the one in left from the right
print(set3|set4) #prints all unique values from both the sets
print(set3 & set4) #prints only thecommon ones
print(set3 ^ set4) #prints only the not common values