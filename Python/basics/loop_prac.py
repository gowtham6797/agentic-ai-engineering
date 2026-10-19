list1=['a','b','c','d','e']

i=0
n=len(list1)
while i<n:
    print(list1[i])
    i+=1

print('')

for value in list1:
    print(value)

print('')

for val in range(10):
    if val % 2!=0:
        continue
    if val == 6:
        break
    print(val)

print('Bye!')