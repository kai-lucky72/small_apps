def linear_search (arr, target):
    for i in range(len(arr)):

        if arr[i] == target:
            return i


arr = [2,3,4,5,6,7,8,9,35,23,24,4,234,554,34,423,534]
target = 23

print(linear_search(arr, target))

def binary_search(arr ,start, end , target):
    while start <= end:

        mid = (start + end) // 2
        if arr[mid] > target:
            start = mid - 1
        elif arr[mid] < target:
            end = start -1

        else:
            return mid

    return start

arr = [2,4,8,10,16,22,25]
target = 10


result = binary_search(arr=arr,start=0,end= len(arr)-1, target=target)

if result != -1:
    print("element is present at index %d" % result)

else:
    print("element isnot in the array please search other way")



def buble_sorting(arr)