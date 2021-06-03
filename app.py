from array import *
a = array('i', [5, 8, 9, 67, 7])
for x in a:
    print(x)
print("the number at first index is ", a[0])
print('the number of elements in the given array is', a.__len__())
a.insert(1,57)
for x in a:
    print(x)
a.remove(7)
for x in a:
    print(x)
b = [4,5,6,7,8,9,2,3,33,44,55,56]
print("Array before revesal is " , b)
print("Array before revesal is ", a)
a.reverse()
b.reverse()
print("Array after revesal is : ", a)
print("Array after revesal is : ", b)
print(len(a))
print(len(b))
max_a = a[0]
for x in range(0,len(a)):
    if(a[x]>max_a):
        max = arr[x]
print(max_a , "is largest among array in a")
max_b = b[0]
for x in range(0,len(b)):
    if(b[x]>max_b):
        max_b = arr[x]
print(max_b , "is largest among array in b")

