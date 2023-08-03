arr = [25,11,7,75,89]
min = arr[0]
for i in range(0,len(arr)):
    if(arr[i]<min):
        min=arr[i]
print("the given array is",arr)
print("minimum value present in give list "+str(min))


