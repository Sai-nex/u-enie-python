import math
print('Napíš hodnoty koeficientov pre a, b aj c')
a = int(input('Hodnota koeficientu a je '))
b = int(input('Hodnota koeficientu b je '))
c = int(input('Hodnota koeficientu c je '))
d = b ** 2 -4 * a * c
print('Diskriminant je číslo', d)

print('Teraz vyrátame aj hodnoty x1 a x2')
dn = math.sqrt(d)
x1 = (-b + dn) / (2*a)
print(x1)
x2 = (-b - dn) / (2*a)
print(x2)
print('hotovo')