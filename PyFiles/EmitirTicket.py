import os


def emitir(
    nombre,
    apellido,
    localidad,
    direccion,
    producto,
    cantidad,
    precio_unitario,
    precio_total,
    forma_pago,
    fecha,
):
    if " " in producto:
        producto = producto.replace(" ", ".")
    if " " in localidad:
        localidad = localidad.replace(" ", ".")
    if " " in direccion:
        direccion = direccion.replace(" ", ".")
    datos = (
        nombre
        + " "
        + apellido
        + " "
        + localidad
        + " "
        + direccion
        + " "
        + producto
        + " "
        + str(cantidad)
        + " "
        + str(precio_unitario)
        + " "
        + str(precio_total)
        + " "
        + forma_pago
        + " "
        + str(fecha)
        + ","
        + "\n"
    )

    if not os.path.exists("assets/txt/tickets.txt"):
        f = open("assets/txt/tickets.txt", "w")
    else:
        f = open("assets/txt/tickets.txt", "a")
    f.write(datos)
    f.close()
