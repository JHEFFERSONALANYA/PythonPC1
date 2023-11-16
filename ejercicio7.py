num_1=int(input("Ingrese el primer número: "))
num_2=int(input("Ingrese el segundo número: "))
print("1=SUMA\n2=RESTA\n3=MULTIPLICACION\n4=DIVISION")
opc=int(input("Ingrese una de las opciones: "))
if opc==1:
    total=num_1+num_2
    print(f'La suma entre {num_1} y {num_2} es: {total}')
elif opc==2:
    total=num_1-num_2
    print(f'La resta entre {num_1} y {num_2} es: {total}') 
elif opc==3:
    total=num_1*num_2
    print(f'La multiplicación entre {num_1} y {num_2} es: {total}')
elif opc==4:
    if num_2==0:
        print("División entre 0, intente de nuevo")
    else:    
        total=num_1/num_2
        print(f'La division de {num_1} entre {num_2} es: {total}')      
else: 
    print("Opción incorrecta")           
    
