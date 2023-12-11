def LongestLen(a):
    str1 = a.split()
    max1 = len(str1[0])
    temp = str1[0]

    for i in str1:
        if(len(i)>max1):
            max1= len(i)
            temp=i

    print("The word with longest length is",temp,"having length", max1)

def CountOccur(a,char):
    count =0
    for i in a:
        if i == char:
            count= count+1

    print("Frequency of character", char, "is", count)

def isPalindrome(a):
    for i in range(0, int(len(a)/2)):
        if a[i] != a[len(a) - i -1]:
            return False
        return True
    
def SubStr(strmain, sub):
    if sub in strmain:
        index = strmain.find(sub)
        print("First appearance of substring", sub, "is at index",index)
    else:
        print("Substring not in string")

def MaxFreq(str):
    a=str.split()
    i =0
    Max =0 
    print("Word | Frequency")
    for j in a:
        if (a.index(j)==i):
            print(j," | ",a.count(j))
        i+=1
            




# str = input("Enter the String to check the word with longest length: ")
# LongestLen(str)

# b = input("Enter the you want to check its frequency: ")
# CountOccur(str, b)

# str2 = input("Enter the String to check the palindrome: ")
# pal = isPalindrome(str2)
# if pal == True:
#     print("String is Palindrome")
# else:
#     print("String is not Palindrome")

# str3 = input("Enter string for checking first appearance of substring: ")
# sub = input("Enter substring: ")
# SubStr(str3, sub)

str4 = input("Enter the string to check frequency: ")
MaxFreq(str4)