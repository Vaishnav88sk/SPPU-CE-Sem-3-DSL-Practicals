def Linear(a,key):
    if key in a:
        for i in range(0,len(a)):
            if a[i] == key:
                print(key,"is found at index",i)
    else:
        print("Not Found!")

def Sentinel(a,key):
    n=len(a)
    last=a[n-1]
    a[n-1]=key
    i=0
    while a[i]!=key:
        i+=1

    a[n-1]=last
    if i<n-1 or key==last:
        print("Element found at",i)
    else:
        print("Element not Found!")