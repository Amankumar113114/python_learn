n=int(input("enter number : "))

for i in range(2,n):
  if(n%i)==0:
         print("not a prime number")
         break
if n==1:
     print("not a prime number")
else:
    print("this is a prime number")    