a = float(input("Peso de A: "))
b = float(input("Peso de B: "))
c = float(input("Peso de C: "))

if a > b and a > c:
    print("A tiene el mayor peso.")
elif b > a and b > c:
    print("B tiene el mayor peso.")
elif c > a and c > b:
    print("C tiene el mayor peso.")
else:
    print("Las esferas tienen pesos iguales.")
