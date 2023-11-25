import json

def cargar_datos():
    with open('output.json', 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    return datos

def encontrar_menor_precio(libros):
    return min(libros, key=lambda x: x.get("Precio", 0))

def encontrar_mayor_precio(libros):
    return max(libros, key=lambda x: x.get("Precio", 0))

def ordenar_por_precio_ascendente(libros):
    return sorted(libros, key=lambda x: x.get("Precio", 0))

def ordenar_por_precio_descendente(libros):
    return sorted(libros, key=lambda x: x.get("Precio", 0), reverse=True)

def ordenar_alfabeticamente(libros):
    return sorted(libros, key=lambda x: x.get("Titulo", "").lower() if x.get("Titulo") is not None else "")

def imprimir_libro(libro):
    titulo = libro.get("Titulo", "Sin título")
    precio = libro.get("Precio", "Precio no disponible")
    disponibilidad = libro.get("Disponibilidad", "Disponibilidad no disponible")
    enlace = libro.get("Enlace", "Enlace no disponible")
    print(f"Libro: {titulo}, Precio: {precio}, Disponibilidad: {disponibilidad}, Enlace: {enlace}")

def main():
    datos = cargar_datos()

    while True:
        print("\n--- Menú ---")
        print("1. Encontrar el libro con el menor precio")
        print("2. Encontrar el libro con el mayor precio")
        print("3. Ordenar de menor a mayor por precio")
        print("4. Ordenar de mayor a menor por precio")
        print("5. Ordenar alfabéticamente por título")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            libro_menor_precio = encontrar_menor_precio(datos)
            imprimir_libro(libro_menor_precio)
        elif opcion == '2':
            libro_mayor_precio = encontrar_mayor_precio(datos)
            imprimir_libro(libro_mayor_precio)
        elif opcion == '3':
            libros_ordenados_ascendente = ordenar_por_precio_ascendente(datos)
            for libro in libros_ordenados_ascendente:
                imprimir_libro(libro)
        elif opcion == '4':
            libros_ordenados_descendente = ordenar_por_precio_descendente(datos)
            for libro in libros_ordenados_descendente:
                imprimir_libro(libro)
        elif opcion == '5':
            libros_ordenados_alfabeticamente = ordenar_alfabeticamente(datos)
            for libro in libros_ordenados_alfabeticamente:
                imprimir_libro(libro)
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
