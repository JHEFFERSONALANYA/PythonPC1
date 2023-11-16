consumo=float(input("Introduzca ¿Cuáto ha consumido en el restaurante (en soles)?: "))
propina=float(input("Introduzca ¿Cuánto porcentaje quiere dejar de propina (OJO: debe ser mayor al 15%)?: "))
total_propina=consumo*propina/100
print(f'La propina total que dejó es: {total_propina} soles')