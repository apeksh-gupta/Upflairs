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

def rightAnglePattern(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end="")
        print()        
       
x = int(input('Enter No. Of Rows : ' ))
rightAnglePattern(x)

        
def multiplication_table(n):
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')

x = int(input('Enter a number : '))
multiplication_table(x)
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

def Counter(s):




def counter(S):
    char_counts = {}
    for char in S:
           char_counts[char] = char_counts.get(char, 0) + 1

    for char, count in char_counts.items():
        print(f"{char} -> {count}")

S = "upflairs pvt ltd"
counter(S)

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




