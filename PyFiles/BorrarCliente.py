from tkinter import *
from tkinter import messagebox


def borrar(selection, nombre, apellido, destroy, eliminar_tree):
    respuesta = messagebox.askokcancel(
        "¿Seguro?", f"¿Seguro que quiere eliminar el cliente {nombre + ' ' + apellido}?"
    )
    if respuesta:
        try:
            f = open("assets/txt/clientes.txt", "r")
            lineas = f.readlines()
            f.close()

            f = open("assets/txt/clientes.txt", "w")

            pos = int(selection)
            linea = lineas[pos]
            lineas.remove(linea)
            for linea in lineas:
                f.write(linea)
            f.close()
            messagebox.showinfo(
                "Cliente eliminado",
                f"Cliente {nombre + ' ' + apellido} eliminado con exito.",
            )
            eliminar_tree()
            destroy.destroy()
        except IndexError:
            pass
    else:
        pass


def borrar_producto(selection, destroy, eliminar_tree):
    respuesta = messagebox.askokcancel(
        "¿Seguro?", f"¿Seguro que quiere eliminar el producto?"
    )
    if respuesta:
        try:
            f = open("assets/txt/productos.txt", "r")
            lineas = f.readlines()
            f.close()

            f = open("assets/txt/productos.txt", "w")

            pos = int(selection)
            linea = lineas[pos]
            lineas.remove(linea)
            for linea in lineas:
                f.write(linea)
            f.close()
            messagebox.showinfo(
                "Producto eliminado",
                f"Producto eliminado con exito.",
            )
            eliminar_tree()
            destroy.destroy()
        except IndexError:
            pass
    else:
        pass
