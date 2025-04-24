edad = int(input("ingrese su edad:" ))

licencia = input("¿tienes licencia de conduccion?(si/no):").lower()

if edad >=18 and licencia:
    print("puede conducir")
else:
    print("no puede conducir caballo")