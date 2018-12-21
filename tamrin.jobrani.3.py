print("Common divisor :مقسوم علیه های مشترک")
a=int(input("enter  first number : "))
b=int(input("enter  second number : "))

if a>b:
    a,b=b,a
for k  in range(1,a+1):
    if(a%k==0)and(b%k==0):
        print(k)
