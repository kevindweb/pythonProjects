print("Please input numbers separated by commas.")
dimensions = [int(x) for x in input().split(",")]
arr = []
for i in range(0,dimensions[0]):
    arr2 = []
    for x in range(0,dimensions[1]):
        arr2.append(i*x)
    arr.append(arr2)
print("arr",arr)
