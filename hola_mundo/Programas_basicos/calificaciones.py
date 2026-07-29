# Clasificación de calificaciones
calificacion = float(input("Ingrese la calificación: "))
if calificacion >= 90:
    letra = "A"
elif calificacion >= 80:
    letra = "B"
elif calificacion >= 70:
    letra = "C"
elif calificacion >= 60:
    letra = "D"
else:
    letra = "F"
print("La calificación es:", letra)