# 1. Write a Python function called is palindrome that takes a string s as input and returns True if s 
# is a palindrome (reads the same forwards and backwards), otherwise returns False.

def is_palindrome(s):
    left = 0 
    right=len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

x = input("Enter your word")
print(is_palindrome(x))

2. Write a Python function called calculator that takes three arguments: num1 (float), num2 (float), 
and operation (string). The function should perform the specified operation ('add', 'subtract', 
'multiply', 'divide') on num1 and num2 and return the result


def calculator( num1 ,  num2 , operation  ):
    
    if operation == 'Add':
        print(f'Addition of {num1} and {num2} : {num1+num2}')
    if operation == 'Subtraction':
        print(f'Difference of {num1} and {num2} : {num1-num2}')
    if operation == 'Multiplication':
        print(f'Multiplication of {num1} and {num2} : {num1*num2}')
    if operation == 'Division1':
        print(f'Division of {num1} and {num2} : {num1/num2}')

x = int(input("enter first number : "))
y = int(input("enter second number : "))
z = input("enter operation to be performed : ")
calculator(x,y,z)


3. Write a python function called word Counter that takes a string “S” as an input, and return the 
count of each character in word or in “S”.
e.g pass S = “upflairs pvt ltd”
u -> 1
p -> 2
l -> 2
and so on 


lst = list()
def Counter(str12):
    for i in str12:
        lst.append(i)
    print(lst)
    for i in lst:
        if i!=lst[len(lst) - 1]:
            return False
    return True 
x = input("Enter your String : ")
y = Counter(str12=x)
print(y)


# 4. Write a Python function called right_triangle_pattern that takes an integer n as input and prints 
# a right triangle pattern of n rows. Each row should contain i asterisks (*), where i is the row 
# number.
# Example: For n = 5, the pattern should be:
# *
# * *
# * * *
# * * * *
# * * * * *

def rightAnglePattern(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end="")
        print()        
       
x = int(input('Enter No. Of Rows : ' ))
rightAnglePattern(x)



# 5. Write a Python function called multiplication_table that takes an integer n as 
# input and prints the multiplication table of n up to 10.
       
def multiplication_table(n):
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')

x = int(input('Enter a number : '))
multiplication_table(x)










