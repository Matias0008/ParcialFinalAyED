import os


def agregar_cliente_archivo(
    nombre, apellido, dni, correo, telefono, localidad, direccion, cp
) -> None:
    # Validacion para saber si el archivo ya existe.
    if not os.path.exists("assets/txt/clientes.txt"):
        f = open("assets/txt/clientes.txt", "w")
    else:
        f = open("assets/txt/clientes.txt", "a")
    direccion = direccion.replace(" ", ".")
    localidad = localidad.replace(" ", ".")
    datos = (
        nombre
        + " "
        + apellido
        + " "
        + telefono
        + " "
        + correo
        + " "
        + dni
        + " "
        + localidad
        + " "
        + direccion
        + " "
        + cp
        + ","
        + "\n"
    )
    try:
        f.write(datos)
        f.close()
    except:
        pass
