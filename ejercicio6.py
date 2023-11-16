edad=int(input("Introduzca su edad: "))
if  edad<4:
    print("Usted entra gratis")
elif edad>=4 and edad<18:
    precio=5
    print(f'Usted debe pagar {precio} soles')
elif edad>=18:
    precio=10
    print(f'Usted debe pagar {precio} soles')                   