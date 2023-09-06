v1 = float(input("departamento 1: "))
v2 = float(input("departamento 2: "))
v3 = float(input("departamento 3: "))
s = float(input("Salario mensual"))

ventas_totales = v1 + v2 + v3
adicional = 0

if v1 > (ventas_totales * 0.33):
    adicional += 0.20 * s

if v2 > (ventas_totales * 0.33):
    adicional += 0.20 * s

if v3 > (ventas_totales * 0.33):
    adicional += 0.20 * s

total_salario = s + adicional

print("Los vendedores reciben:", total_salario)
