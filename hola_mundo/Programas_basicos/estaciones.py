# Estaciones del año
mes = int(input("Ingrese el número del mes (1-12): "))
match mes:
    case 12 | 1 | 2:
        estacion("Es invierno.")
    case 3 | 4 | 5:
        estacion("Es primavera.")  
    case 6 | 7 | 8: 
        estacion("Es verano.")
    case 9 | 10 | 11:
        estacion("Es otoño.")
    case _:
        estacion("Número de mes inválido.")
        print("Estaccion", estacion)
