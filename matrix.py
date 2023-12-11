# Addition of two Matrices

def addition(mat1,mat2,r,c):
    addition =[]
    for i in range(r):
        subList=[]
        for j in range(c):
            sum= mat1[i][j]+ mat2[i][j]
            subList.append(sum)
        addition.append(subList)
    return addition

def crMatrix(mat,r,c):
    for i in range(r):
        row=[]
        for j in range(c):
            element = int(input("Enter elements of matrix: "))
            row.append(element)
        mat.append(row)

def call_mat1():
    mat1=[]
    r = int(input("Enter number of rows:"))
    c = int(input("Enter number of columns:"))
    crMatrix(mat1,r,c)

def call_mat2():
    mat2=[]
    r = int(input("Enter number of rows:"))
    c = int(input("Enter number of columns:"))
    crMatrix(mat2,r,c)


# Subtraction of two Matrices 

def subtraction(mat1,mat2,r,c):

    subtraction =[]
    for i in range(r):
        subList=[]
        for j in range(c):
            sub = mat1[i][j]-mat2[i][j]
            subList.append(sub)
        subtraction.append(subList)
    return subtraction


# Multiplication of two Matrices 
def call_mul1():
    print("Enter Row and Column size of First Matrix: ",end="")
    r1=int(input())
    c1=int(input())
    print("Enter"+str(r1*c1)+"Elements:",end="")

    mat1=[]
    for i in range(r1):
        mat1.append([])
        for j in range(c1):
            num=int(input())
            mat1[i].append(num)

def call_mul2():
    print("Enter Row and Column size of Second Matrix: ",end="")
    r2=int(input())
    c2=int(input())
    print("Enter"+str(r2*c2)+"Elements:",end="")

    mat2=[]
    for i in range(r2):
        mat2.append([])
        for j in range(c2):
            num=int(input())
            mat2[i].append(num)
def mult(mat1,mat2,r1,c1,r2,c2):
    mat3 =[]
    for i in range(r1):
        mat3.append([])
        for j in range(c2):
            sum=0
            for k in range(c1):
                sum = sum+(mat1[i][k]*mat2[k][j])
            mat3[i].append(sum)

    print("\n Multiplication of given matrix is:")
    for i in range(r1):
        for j in range(c2):
            print(mat3[i][j],end="")
        print()
    
# Transpose of two Matrices    

def call_transpose():
    r=int(input("Enter the Number  the rows: "))
    c=int(input("Enter the Number of columns: "))

    print("Enter the elements of matrix: ")
    matrix=[[int(input()) for i in range(c)] for i in range(r)]
    print("Your Matrix is: ")
    for n in matrix:
        print(n)

def transpose(matrix,r,c):
    result=[[0 for i in range(r)]for j in range(c)]
    for i in range(r):
        for j in range(c):
            result[i][j]= matrix [j][i]

    print("Transpose of matrix is :")
    for r in result:
        print(r)

