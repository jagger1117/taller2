lado1=float(input())
lado2=float(input())
lado3=float(input())
perimetro=lado1+lado2+lado3
semi=perimetro/2
area=(semi * (semi - lado1) * (semi - lado2) * (semi - lado3))**(0.5)

print("perimetro", perimetro)
print("semi",semi)
print("area",area)