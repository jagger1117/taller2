nombre=str(input("nombre"))
codigo=input("")
horas=int(input(""))
valorHora=int(input(""))
retencion=int(input(""))

salariob=(horas*valorHora)
salarion=salariob-((salariob*retencion)/100)

print("codigo",codigo)
print("nombre",nombre)
print("salariob",salariob)
print("salarion",salarion)