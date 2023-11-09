#formula cuadratica
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))


raiz1 = (-b+(b**2 - 4*a*c))/(2*a)
raiz2 = (-b-(b**2 - 4*a*c))/(2*a)

print(raiz1)
print(raiz2)