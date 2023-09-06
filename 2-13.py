color = input("color de la bolita")
total_compra = float(input("valor total "))

descuento = 0

if color == "verde":
    descuento = 0.10
elif color == "amarilla":
    descuento = 0.25
elif color == "azul":
    descuento = 0.50
elif color == "roja":
    descuento = 1.00

monto_final = total_compra * (1 - descuento)
print("El cliente debe pagar ", monto_final)
