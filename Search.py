# linear seach
# 1 1 kerke sab ko search ker dungi
# a=[1,2,3,4,5,6,7]
# for i in a:
#     if i==5:
#         print(i,"Found")
#         continue
#     else:
#         continue
#         print("Not Found")

# binary search
# binary search can be done only in sorted array


def binary_search(arr,x):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(end+start)//2
        if arr[mid]== x:
            return mid
        elif arr[mid]>x:
            end= mid-1
        else:
            start=mid+1
    return -1

arr=[10,20,30,30,30,60,70,80,90]
x=30
print(binary_search(arr,x))

