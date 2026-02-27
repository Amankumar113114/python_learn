# greatest of three number
def greatest(a,b,c):
    if a>b and a>c:
        result=print(f"the greatest number is {a}")
    elif b>a and b>c:
        result=print(f"the greatest number is {b}")
    else:
        result=print(f"the greatest number is {c}")

    return result
try:
    num1=float(input("enter 1st number:"))
    num2=float(input("enter 2nd number:"))
    num3=float(input("enter 3rd number:"))
    greatest(num1,num2,num3)
except(ValueError):
    print("please enter  numbers")
