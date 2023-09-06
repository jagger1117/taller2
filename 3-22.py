n = input("Nombre: ")
s = float(input("Salario por hora: "))
h = float(input("Horas trabajadas en el mes: "))

m = s * h

if m > 450000:
    print(n, m)
else:
    print(n)
