a = int(input("primer numero: "))
b = int(input("segundo numero: "))
c = int(input("tercer numero: "))

if a > b:
    if a > c:
        mayor = a
    else:
        mayor = c
else:
    if b > c:
        mayor = b
    else:
        mayor = c

print("El numero mayor es:", mayor)