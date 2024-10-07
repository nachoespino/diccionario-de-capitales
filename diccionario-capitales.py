import json
import os

#Función para cargar el diccionario desde el archivo json
def cargar_diccionario():
    ruta = os.path.join('proyectos', 'capitales', 'data.json')
    if os.path.exists(ruta):
        with open(ruta , 'r', encoding='utf-8') as file:
            return json.load(file)
    return{} #Devolver un diccionario vacío en caso de que no exista el archivo

#Función para guardar el diccionario en un archivo
def guardar_diccionario(diccionario):
    ruta = os.path.join('proyectos', 'capitales', 'data.json')
    with open(ruta , 'w', encoding='utf-8') as file:
        json.dump(diccionario, file, indent=4, ensure_ascii=False, sort_keys=True)
    cargar_diccionario()
    return diccionario

#Función para actualizar el diccionario
def actualizar_diccionario(diccionario):
    #Pedir un dato al usuario
    pais = input("Introduce un país: ")
    capital = input("Introduce su capital: ")
    #Agregar el dato al diccionario
    diccionario[pais] = capital
    #Guardar el diccionario actualizado
    guardar_diccionario(diccionario)
    print("País y capital agregados exitosamente.")
    elegir_accion(diccionario)
    return diccionario

#Función para consultar el diccionario
def consultar_diccionario(diccionario):
    pais = input("\n\nIntroduce un país:")
    if pais in diccionario:
        print("La capital de" , pais , "es" , diccionario.get(pais))
    else:
        print("No sé la capital de ese país.")
    elegir_accion(diccionario)
    return diccionario

#Función para elegir acción
def elegir_accion(diccionario):
    diccionario = dict(sorted(diccionario.items())) #Con esta línea ordenamos el diccionario alfabéticamente en memoria
    accion = input("\nMENÚ:\n1. Consultar diccionario.\n2. Actualizar diccionario.\n3. Mostrar diccionario.\n4. Salir.\n\nIntroduce el número de la opción deseada: ")
    while True:
        if(accion == "1"):
            consultar_diccionario(diccionario)
            break
        elif(accion == "2"):
            actualizar_diccionario(diccionario)
            break
        elif(accion == "3"):
            print('\n')
            for pais, capital in diccionario.items():
                print(f'{pais} - {capital}')
            elegir_accion(diccionario)
            break
        elif(accion == "4"):
            print("\n\n||||||||||||||||||||||||||||||||||||||||")
            print("        ·•Hasta la vista, baby•·")
            print("||||||||||||||||||||||||||||||||||||||||\n\n")
            break
        else:
            accion = input("\nEntrada no válida.\n\nMENÚ:\n1. Consultar diccionario.\n2. Actualizar diccionario.\n3. Mostrar diccionario.\n4. Salir.\n\nIntroduce el número de la opción deseada: ")

#Cargar el diccionario
diccionario = cargar_diccionario()

#Menú de la aplicación
print("\n\n||||||||||||||||||||||||||||||||||||||||")
print(" Bienvenido al diccionario de capitales")
print("||||||||||||||||||||||||||||||||||||||||\n\n")

elegir_accion(diccionario)