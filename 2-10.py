numero_inscripcion = input()
nombres = input()
patrimonio = float(input())
estrato_social = int(input())
pago_matricula = 50000

if patrimonio > 2000000 and estrato_social > 3:
    pago_matricula += 0.03 * patrimonio

print("Número de inscripción:", numero_inscripcion)
print("Nombres:", nombres)
print("Pago de matrícula:", pago_matricula)