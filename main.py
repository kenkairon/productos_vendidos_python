"""
Programa para buscar las cantidad vendidas de un producto
"""

ventas = [("Laptops", 3), ("Celulares", 5), ("Monitores", 2), ("Teclados", 4)]

while True:
    try:
        consulta = int(input(
            "Las ventas de qué productos quiere conocer:\n"
            "1-Laptop\n"
            "2-Celular\n"
            "3-Monitor\n"
            "4-Teclado\n"
        ).strip()) # para eliminar espacios en blanco al momento de ingresar

        arreglo = consulta - 1

        if 0 <= arreglo < len(ventas):
            for indice, producto in enumerate(ventas):
                if arreglo == indice:
                    print(f"El total de {producto[0]} vendido fue {producto[1]}")
                    break  # Sale del for cuando encuentra el producto
            break  # Sale del while cuando la opción es válida

        print("La opción no es válida, seleccione un número entre 1 y 4")

    except ValueError:

        print("El valor no es correcto, ingrese una opción numérica del producto por favor")
        