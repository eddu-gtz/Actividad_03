lista = []

while True:
    print("1. Agregar")
    print("2. Mostrar")
    print("0. Salir")
    op = input()

    if op == "1":
        nombre = input("Nombre: ")
        lista.append(nombre)
    elif op == "2":
        for n in lista:
            print(n)
    elif op == "0":
        break
