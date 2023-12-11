def average(a):
    sum =0
    count = 0
    for i in range (len(a)):
        if a[i]>0:
            sum = sum + a[i]
            count +=1

    avg = sum/count
    print("Total Marks: ", sum)
    print("Average marks: ",avg)


def Highest(a):
    for i in range(len(a)):
        if a[i]>0:
            Max = a[0]
        break
    for i in range(1,len(a)):
        if a[i]>Max:
            Max = a[i]
        
    return Max

def Lowest(a):
    for i in range(len(a)):
        if a[i]>0:
            Min = a[0]
        break
    for i in range(1,len(a)):
        if a[i]<Min:
            Min = a[i]
        
    return Min

def Absent(a):
    count =0
    for i in range(len(a)):
        if a[i]<0:
            count +=1
    return count

def MaxFreq(a):
    i =0
    Max =0 
    print("Marks | Frequency")
    for j in a:
        if (a.index(j)==i):
            print(j," | ",a.count(j))
            if a.count(j)>Max:
                Max=a.count(j)
                mark=j
        i=i+1
    print(mark,"have highest frequency ", Max)
    return(mark,Max)


a=[2,4,6,4,8,10,4]
MaxFreq(a)


    

