# find the factorial of a number using a function
def factorial(num1):
    if num1==1 or num1==0:
        return 1
    else:
        return num1*factorial(num1-1)
print("the factorial of my number is :",str(factorial(5)))