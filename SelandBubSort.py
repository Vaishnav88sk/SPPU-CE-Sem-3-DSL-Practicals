def SelectionSort(marks):
    for i in range (len(marks)):
        min_ind=i
        for j in range(i+1, len(marks)):
            if marks[min_ind]>marks[j]:
                min_ind=j
        marks[min_ind],marks[i]=marks[i],marks[min_ind]


    for i in range(len(marks)):
        print(marks[i])

def BubbleSort(marks):
    n = len(marks)
    for i in range(n-1):
        for j in range (0, n-i-1):
            if marks[j]>marks[j+1]:
                marks[j],marks[j+1]=marks[j+1],marks[j]
    for i in range(len(marks)):
        print(marks[i])

def top_five(marks):
    n= len(marks)
    Maximum = n-1
    Minimum = n-6
    print(marks[Maximum:Minimum:-1])

mark=[7,3,4,90,15,36,67]
BubbleSort(mark)
top_five(mark)
