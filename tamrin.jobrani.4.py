import math

x1 = int(input("::  مولفه x نقطه اول را وارد کنید"))
y1 = int(input("::  مولفه y نقطه اول را وارد کنید"))
x2 = int(input("::  مولفه x نقطه دوم را وارد کنید"))
y2 = int(input("::  مولفه y نقطه دوم را وارد کنید"))
x3 = int(input("::  مولفه x نقطه سوم را وارد کنید"))
y3 = int(input("::  مولفه y نقطه سوم را وارد کنید"))
a = math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))#بدست آوردن اندازه اضلاع
b = math.sqrt(math.pow((x3-x1),2)+math.pow((y3-y1),2))
c = math.sqrt(math.pow((x2-x3),2)+math.pow((y2-y3),2))
p = (a+b+c)//2
area = math.sqrt(p*(p-a)*(p-b)*(p-c)) #فرمول هرون
print(" :: محیط ",2*p)
print(" :: مساحت ",area)