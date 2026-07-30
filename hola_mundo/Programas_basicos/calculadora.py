#Calculadora Básica
while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    op = int(input("Opción: "))
    if op == 5:
        break
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    match op:
        case 1:
            print(a + b)
        case 2:
            print(a - b)
        case 3:
            print(a * b)
        case 4:
            if b != 0:
                print(a / b)
            else:
                print("Error: división por cero")
    resp = input("¿Desea continuar? (s/n): ").lower()
    if resp == "n":
        break