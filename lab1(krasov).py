import math

print("Введите коэфициенты квадратного уравнения")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

z = (b*b-4.0*a*c)
d = math.sqrt(z)
x1 = 0
x2 = 0
if d>0:
    x1 = ((-b) + d)/(2.0*a)
    x2 = ((-b) - d)/(2.0*a)
    print("x1 = %.2f\nx2 = %.2f" % (x1, x2))
elif d==0:	
    x= (-b)/(2.0*a)
    print("x = %.2f" % x)
else:
    print("Nope sqrt")

    exit=input('Нажмите ENTER')
