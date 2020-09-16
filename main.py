while True:
    print("1. Agregar")
    print("2. Mostrar")
    print("0. Salir")
    op = input()

    if op == "1":
        nombre = input("Nombre: ")
    elif op == "2":
        print(nombre)
    elif op == "0":
        break
