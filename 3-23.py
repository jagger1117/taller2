a = float(input("Valor de A "))
b = float(input("Valor de B "))
c = float(input("Valor de C "))

discriminante = b**2 - 4*a*c

if discriminante > 0:
    x1 = (-b + discriminante**0.5) / (2*a)
    x2 = (-b - discriminante**0.5) / (2*a)
    print("Las soluciones son:", x1, "y", x2)
elif discriminante == 0:
    x1 = -b / (2*a)
    print("La solucion unica es:", x1)
else:
    print("No hay soluciones reales.")
