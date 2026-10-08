from funciones import validador
apellido = str(input("Ingrese el apellido del jugador: "))
nacimiento = int(input("Ingrese el año de nacimiento: "))
altura = int(input("Ingrese la altura en cm: "))
persona = [apellido, nacimiento, altura]
resultado = validador(persona)
if resultado[0]:
    print("Nacido en 2010 o mas")
else:
    print("No cumple con el año de nacimiento")
if resultado[1]:
    print("Cumple con la altura")
else:
    print("No cumple con la altura")