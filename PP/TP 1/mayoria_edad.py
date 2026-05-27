from datetime import datetime, date

print("====================================")
print(" Verificador de Mayoría de Edad")
print("====================================")
print("Este programa calcula tu edad y verifica si sos mayor o menor de edad.")

fecha_actual = date.today()
print("Fecha actual:", fecha_actual.strftime("%d/%m/%Y"))

while True:
    fecha_ingresada = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")

    try:
        fecha_nacimiento = datetime.strptime(fecha_ingresada, "%d/%m/%Y").date()

        if fecha_nacimiento > fecha_actual:
            print("Error: la fecha no puede ser futura.")
            continue

        edad_maxima = fecha_actual.year - fecha_nacimiento.year

        if edad_maxima > 120:
            print("Error: fecha no razonable. Máximo 120 años.")
            continue

        break

    except ValueError:
        print("Error: formato incorrecto.")
        print("Ejemplo válido: 15/08/2005")

edad = fecha_actual.year - fecha_nacimiento.year

if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
    edad = edad - 1
    
print("\n========== RESULTADOS ==========")
print("Fecha de nacimiento:", fecha_nacimiento.strftime("%d/%m/%Y"))
print("Edad actual:", edad, "años")

if edad >= 18:
    print("La persona es mayor de edad.")
else:
    faltan = 18 - edad
    print("La persona es menor de edad.")
    print("Le faltan", faltan, "años para cumplir 18.")
    
print("\nGracias por usar el Verificador de Mayoría de Edad.")
print("Programa finalizado.")