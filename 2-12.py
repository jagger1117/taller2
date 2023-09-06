n = input("nombre del trabajador: ")
h = float(input("horas trabajadas"))
v = float(input("valor por hora"))

if h <= 40:
    s = h * v
else:
    hn = 40
    he = h - 40

    if he <= 8:
        s = (hn * v) + (he * v * 2)
    else:
        hed = 8
        het = he - 8
        s = (hn * v) + (hed * v * 2) + (het * v * 3)

print(n, "recibirá un salario de ", s)