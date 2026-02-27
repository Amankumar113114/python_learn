def pattern(n):
    for i in range(1,n+1):
        print("*"*(n+1-i))
try:
    num=int(input("enter a number: "))
    pattern(num)
except:
    print("invalid input")