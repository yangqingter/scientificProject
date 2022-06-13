import numpy as np

arr = np.random.randint(0,10,(3,4))
print(arr)

arr = np.arange(0,12).reshape(3,4)
print(arr)

l1 = arr<5

print(arr<5)

a1=arr[arr<5]
print(arr[arr<5])

print(np.where(arr<5,10*arr,100*arr))

