time=input("Ingrese la hora actual: ")
hours, minutes = time.split(":")
if hours=='7':
    print("Es hora de desayunar")
elif hours=='12':
    print("Es hora de almorzar")
elif hours=='18':
    print("Es hora de cenar")    
