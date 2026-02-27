# celsius to fahrenheit
def cel_to_fahr(a):
    f=(a*1.8)+32
    result=print(f"{a} degree celsius = {f} degree of fahrenheit")
    return  result
try:
    temp=float(input("enter temperature in celsius :"))
    cel_to_fahr(temp)
except:
    print("invalid temperature")