# sum of n number using recursive function
def add(a):
    if a<=0:
       return 0
    else:
        return a+add(a-1)

try:
    num=int(input("enter number :"))
    print(f"the sum of 1 to {num} = {add(num)}")
except(ValueError):
    print("invalid input")
