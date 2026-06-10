# def function_name():
#     code

def greet():
    print("python")
greet()

def square():
    for i in range(5):
        for j in range(5):
            print("*",end="")
        print()
square()
name = input("enter your name")
age = int(input("enter your age"))

def sayHi(name,age):
    print(f"hi -> {name}    your age is {age}")
sayHi(name,age)

def addbyTwo(n):
    return n+2
print(addbyTwo(7))


# local variables 
# down u can see two examples of local variables
# local 1 will and local 2 will not work

# def local1():
#     x = 10
#     print(x)

# local1()

# def loacl2():
#     y = 10

# loacl2()
# print(y) 
# NameError: name 'y' is not defined

# global variables
# up we have done the input of name varible so that vairbales can be used anywhere in this file
print(name)


# see the below example for local vs global variables
# x is declared  in global and even inside the test function
# so now this x variable works diffrent in both cases
# cases - 1  x is called and declred in test function 
# case 2 x again called outside the test function
x = 100

def test():
    x = 50
    print(f" inisde the test funtion ==>{x}")

test()

print(f" outside the test funtion ==>{x}")


# Recursion functions
def countdown(n):

    if n == 0:
        return
# this above n == 0 is base case 
# base case means A stopping condition
    print(n)

    countdown(n - 1)

countdown(5)