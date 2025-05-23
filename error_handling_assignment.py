#divide function that keeps looping until right numbers are entered
def divide():
    while True  :
        try:
            num1,num2=(input("enter num1 ")), (input("enter num2 "))
            result=int(num1)/int(num2)
        except ValueError:
            print("the numbers cant be divided")
        except ZeroDivisionError:
            print("we cant divide by zero")
        else:
            print(result)
            break

#call the function   
divide()