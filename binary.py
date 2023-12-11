def binary(a,key):
    low=0
    high=len(a)-1

    while low<=high:
        mid=int((low+high)/2)
        if key<a[mid]:
            high = mid-1
        elif key>a[mid]:
            low = mid+1
        else:
            return mid
    return -1

a=[2,4,6,8,10,12]
key=10
ind=binary(a,key)
if ind==-1:
    print("Key is not found")
else:
    print("key is found at index", ind)