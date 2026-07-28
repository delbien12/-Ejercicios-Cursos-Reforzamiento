# Conversor de monedas

cantidad = float(input("Ingrese la cantidad en MXN: "))
print("Monedas: 1. USD 2. EUR 3. THB 4. JPY 5. KRW 6. AUD 7. PEN 8. CAD 9. VEZ 10. ARS")
opcion = int(input("Seleccione la moneda: "))

match opcion:
    case 1:
        resultado = cantidad / 16.5
        manera = "USD"
    case 2:
        resultado = cantidad / 18.0
        manera = "EUR"
    case 3:
        resultado = cantidad / 0.45
        manera = "THB"
    case 4:
        resultado = cantidad / 0.12
        manera = "JPY"
    case 5:
        resultado = cantidad / 0.013
        manera = "KRW"
    case 6:
        resultado = cantidad / 11.5
        manera = "AUD"
    case 7:
        resultado = cantidad / 2.8
        manera = "PEN"
    case 8:
        resultado = cantidad / 8.2
        manera = "CAD"
    case 9:
        resultado = cantidad / 0.0023
        manera = "VEZ"
    case 10:
        resultado = cantidad / 0.046
        manera = "ARS"
    case _:
        print("Opción inválida.")

print("Resultado:", resultado, manera)