from tkinter import messagebox


def editar(selection, old, reemplazar):
    if reemplazar != "":
        if " " in old:
            old = old.replace(" ", ".")
        if " " in reemplazar:
            reemplazar = reemplazar.replace(" ", ".")
        f = open("assets/txt/clientes.txt", "r")
        lineas = f.readlines()

        f.close()

        f = open("assets/txt/clientes.txt", "w")

        pos = int(selection)
        linea = lineas[pos]
        print("linea", linea)
        print("old", old)
        reemplazado = linea.replace(old, reemplazar, 1)
        print("reem", reemplazado)
        for linea in range(len(lineas)):
            if linea == selection:
                f.write(reemplazado)
            else:
                f.write(lineas[linea])
        f.close()
    else:
        pass
