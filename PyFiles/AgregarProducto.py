import os


def agregar_producto(nombre, precio, prefix):
    if not os.path.exists("assets/txt/productos.txt"):
        f = open("assets/txt/productos.txt", "w")
    else:
        f = open("assets/txt/productos.txt", "a")

    if " " in nombre:
        nombre = nombre.replace(" ", ".")

    datos = nombre + " " + precio + " " + prefix + "," + "\n"
    f.write(datos)
    f.close()
