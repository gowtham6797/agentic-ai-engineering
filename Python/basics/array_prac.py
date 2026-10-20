from array import *

arr_len = int(input("Enter the size of the array "))
arr1 = array("i")

for i in range(arr_len):
    num = input("Enter the element ")
    arr1.append(int(num))

print("Array has been generated")

for n in arr1:
    print(n)

arr2 = array(arr1.typecode, (n for n in arr1))

arr2.reverse()

print("Array 2 has been reversed...")

for n in arr2:
    print(n)
