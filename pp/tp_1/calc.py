#                Ejercicio 2 — Conversor de Temperaturas  

# Mostrar un menú al usuario con las opciones: 

# 1) Celsius a Fahrenheit, 

# 2) Fahrenheit a Celsius, 

# 3) Salir.

# Solicitar al usuario que elija una opción del menú.

# Solicitar al usuario que ingrese la temperatura a convertir.
# v
# Realizar la conversión correspondiente usando las fórmulas: 

# F = C × 9/5 + 32 y C = (F - 32) × 5/9.

# Mostrar el resultado de la conversión con un decimal de precisión.

# El programa debe repetirse hasta que el usuario elija la opción "Salir".

# Archivo sugerido: conversor_temperaturas.py

def convert(type_to, value):
    output = 0
    
    if (type_to == 'F'):
        output = value * 1.8 + 32
        
    elif (type_to == 'C'):
        output = (value - 32) * 5/9
        
    return output


while (True):
    initial_value = int(input('Ingresá la opcion 1. C to F 2. F to C 3. Exit'))
    
    match initial_value:
        case 1:
            to_fahr = float(input('Ingresá el valor a convertir'))
            print(convert('F', to_fahr))
        case 2:
            to_cel = float(input('Ingresá el valor a convertir'))
            print(convert('C', to_cel))
        case 3:
            print('Saliendo...')
            break
        case _:
            print('Opcion Invalida')