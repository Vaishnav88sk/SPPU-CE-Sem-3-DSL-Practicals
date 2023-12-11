def removedup(d):
    lst=[]
    for i in d:
        if i not in d:
            lst.append(i)
    return lst

def intersection(lst1,lst2):
    lst3=[]
    for i in lst1:
        if i in lst2:
            lst3.append(i)
    return lst3
def union(lst1,lst2):
    lst3=[]
    lst3=lst1.copy()
    for i in lst2:
        if i not in lst3:
            lst3.append(i)
    return lst3

def diff(lst1,lst2):
    lst3=[]
    for i in lst1:
        if i not in lst2:
            lst3.append(i)
    return lst3

def sym_diff(lst1,lst2):
    lst3=[]
    D1=diff(lst1,lst2)
    D2=diff(lst2,lst1)
    lst3=union(D1,D2)
    return lst3

def CB(lst1,lst2):
    lst3=intersection(lst1,lst2)
    print(lst3)
    return lst3

def eCeB(lst1,lst2):
    lst3=sym_diff(lst1,lst2)
    print(lst3)
    return lst3

def nCnB(lst1,lst2,lst3):
    lst4=diff(lst1,union(lst2,lst3))
    print(lst4)
    return lst4

def CBnF(lst1,lst2,lst3):
    lst4=diff(intersection(lst1,lst2),lst3)
    print(lst4)
    return lst4



