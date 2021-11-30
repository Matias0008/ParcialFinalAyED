from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
from AddClient import agregar_cliente_archivo
from BorrarCliente import borrar_producto
from EditarCliente import editar
from AgregarProducto import agregar_producto
from datetime import datetime
from EmitirTicket import emitir

root = Tk()
root.title("Estacion de servicio - La Llegada")
root.resizable(0, 0)
root.geometry("1500x800")
image = Image.open("assets/img/llegada2.jpg")
image = image.resize((600, 510), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

l = Label(image=img)
l.grid(column=0, row=0, columnspan=2)


def agregar_cliente():
    global nombre_var, apellido_var
    top = Toplevel()
    top.resizable(0, 0)
    top.title("Agregar cliente")
    top.iconbitmap("assets/img/icono-cliente.ico")

    # Creando titulos y entry
    nombre = Label(
        top, text="Nombre", fg="#091540", font=("Helvetica", 11, "bold", "underline")
    )
    nombre_var = StringVar()
    nombre_e = Entry(top, textvariable=nombre_var, width=25, font=10)

    apellido_var = StringVar()
    apellido = Label(
        top, text="Apellido", fg="#091540", font=("Helvetica", 11, "bold", "underline")
    )
    apellido_e = Entry(top, textvariable=apellido_var, width=25, font=10)

    documento = Label(
        top, text="Documento", fg="#091540", font=("Helvetica", 11, "bold", "underline")
    )
    documento_var = StringVar()
    documento_e = Entry(top, textvariable=documento_var, width=25, font=10)

    correo = Label(
        top, text="Correo", fg="#091540", font=("Helvetica", 11, "bold", "underline")
    )
    correo_var = StringVar()
    correo_e = Entry(top, textvariable=correo_var, width=25, font=10)

    telefono = Label(
        top, text="Telefono", fg="#091540", font=("Helvetica", 11, "bold", "underline")
    )
    telefono_var = StringVar()
    telefono_e = Entry(top, textvariable=telefono_var, width=25, font=10)

    direccion = Label(
        top, text="Direccion", fg="#091540", font=("Helvetica", 11, "bold", "underline")
    )
    direccion_var = StringVar()
    direccion_e = Entry(top, textvariable=direccion_var, width=25, font=10)

    localidad = Label(
        top, text="Localidad", fg="#091540", font=("Helvetica", 11, "bold", "underline")
    )
    localidad_var = StringVar()
    localidad_e = Entry(top, textvariable=localidad_var, width=25, font=10)

    cod_postal = Label(
        top,
        text="Codigo postal",
        fg="#091540",
        font=("Helvetica", 11, "bold", "underline"),
    )
    cod_postal_var = StringVar()
    cod_postal_e = Entry(top, textvariable=cod_postal_var, width=25, font=10)

    # Posicionando los elementos mediante grid.
    nombre.grid(column=0, row=0, padx=10, pady=10, columnspan=1)
    apellido.grid(column=0, row=2, padx=10, pady=10)
    documento.grid(column=0, row=3, padx=10, pady=10)
    nombre_e.grid(column=1, row=0, padx=15, pady=15)
    apellido_e.grid(column=1, row=2)
    documento_e.grid(column=1, row=3)
    correo.grid(column=0, row=4, padx=10, pady=10)
    correo_e.grid(column=1, row=4)
    telefono.grid(column=0, row=5, padx=10, pady=10)
    telefono_e.grid(column=1, row=5)
    direccion.grid(column=0, row=6, padx=10, pady=10)
    direccion_e.grid(column=1, row=6)
    localidad.grid(column=0, row=7, padx=10, pady=10)
    localidad_e.grid(column=1, row=7)
    cod_postal.grid(column=0, row=8, padx=10, pady=10)
    cod_postal_e.grid(column=1, row=8)

    def agregar_messagebox(*args):
        global cliente

        # Obteniendo los datos para realizar validacion
        (
            nombre,
            apellido,
            documento,
            correo,
            telefono,
            localidad,
            direccion,
            cod_postal,
        ) = (
            nombre_var.get(),
            apellido_var.get(),
            documento_var.get(),
            correo_var.get(),
            telefono_var.get(),
            localidad_var.get(),
            direccion_var.get(),
            cod_postal_var.get(),
        )

        # Comprobacion de campos vacios
        if (
            not nombre
            or not apellido
            or not documento
            or not correo
            or not telefono
            or not localidad
            or not direccion
            or not cod_postal
        ):
            messagebox.showerror("Error", "Error, los campos son obligatorios.")
            return

        # Pidiendo confirmacion para agregar
        pregunta = messagebox.askyesno(
            "Agregar cliente",
            f"¿Seguro que desea agregar el cliente {nombre + ' ' + apellido}?",
        )

        if pregunta:
            agregar_cliente_archivo(
                nombre,
                apellido,
                documento,
                correo,
                telefono,
                localidad,
                direccion,
                cod_postal,
            )
            if agregar_cliente_archivo:
                messagebox.showinfo("Agregado", "Cliente agregado con éxito.")
                top.destroy()

            render_clientes()
        else:
            pass

    btn_agregar = Button(
        top,
        text="Agregar",
        command=agregar_messagebox,
        font=("Helvetica", 10, "bold"),
        fg="red",
    )
    btn_agregar.grid(column=1, row=9, columnspan=3, pady=10, ipadx=10)
    top.bind("<Return>", agregar_messagebox)


# Creando frame para el treeview
tree_frame = Frame(root)
tree_frame.grid(column=2, row=0, sticky=N)

# Creando treeview
tree = ttk.Treeview(tree_frame)
tree.grid(column=2, row=0, pady=40, padx=5)


# Agregando una scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.grid(column=3, row=0, sticky="nse")
tree_scroll.configure(command=tree.yview)
tree.configure(yscrollcommand=tree_scroll.set)

tree["columns"] = (
    "Nombre",
    "Apellido",
    "Telefono",
    "Correo",
    "DNI",
    "Localidad",
    "Direccion",
    "CP",
)

tree.column("#0", stretch=NO, width=0)
tree.column("Nombre", width=100, anchor=N)
tree.column("Apellido", width=100, anchor=N)
tree.column("Telefono", width=100, anchor=N)
tree.column("Correo", anchor=N)
tree.column("DNI", width=70, anchor=N)
tree.column("Localidad", width=110, anchor=N)
tree.column("Direccion", width=110, anchor=N)
tree.column("CP", width=70, anchor=N)


tree.heading("#0")
tree.heading("Nombre", text="Nombre")
tree.heading("Apellido", text="Apellido")
tree.heading("Telefono", text="Telefono")
tree.heading("Correo", text="Correo")
tree.heading("DNI", text="DNI")
tree.heading("Localidad", text="Localidad")
tree.heading("Direccion", text="Direccion")
tree.heading("CP", text="CP")

titulo_tree = Label(root, text="Clientes", font=("Helvetica", 12, "bold"))
titulo_tree.grid(column=2, row=0, sticky=N, pady=10)


def eliminar_tree():
    x = tree.selection()[0]
    tree.delete(x)


# Nuevo frame para mostrar datos
frame_datos = LabelFrame(
    tree_frame, text="Modificar datos", font=("Helvetica", 12, "bold")
)
frame_datos.grid(column=2, row=1, sticky=W, padx=5, pady=40, columnspan=6)

nombre = Label(
    frame_datos,
    text="Nombre",
    fg="#091540",
    font=("Helvetica", 11, "bold", "underline"),
)

nuevo_nombre = StringVar()
nombre_e = Entry(frame_datos, textvariable=nuevo_nombre, width=25, font=10)
nombre.grid(row=1, column=1)
nombre_e.grid(row=1, column=2)

apellido = Label(
    frame_datos,
    text="Apellido",
    fg="#091540",
    font=("Helvetica", 11, "bold", "underline"),
)
nuevo_apellido = StringVar()
apellido_e = Entry(frame_datos, textvariable=nuevo_apellido, width=25, font=10)

telefono = Label(
    frame_datos,
    text="Telefono",
    fg="#091540",
    font=("Helvetica", 11, "bold", "underline"),
)
nuevo_telefono = StringVar()
telefono_e = Entry(frame_datos, textvariable=nuevo_telefono, width=25, font=10)

correo = Label(
    frame_datos,
    text="Correo",
    fg="#091540",
    font=("Helvetica", 11, "bold", "underline"),
)
nuevo_correo = StringVar()
correo_e = Entry(frame_datos, textvariable=nuevo_correo, width=25, font=10)

documento = Label(
    frame_datos,
    text="Documento",
    fg="#091540",
    font=("Helvetica", 11, "bold", "underline"),
)
nuevo_documento = StringVar()
documento_e = Entry(frame_datos, textvariable=nuevo_documento, width=25, font=10)

direccion = Label(
    frame_datos,
    text="Direccion",
    fg="#091540",
    font=("Helvetica", 11, "bold", "underline"),
)
nueva_direccion = StringVar()
direccion_e = Entry(frame_datos, textvariable=nueva_direccion, width=25, font=10)

localidad = Label(
    frame_datos,
    text="Localidad",
    fg="#091540",
    font=("Helvetica", 11, "bold", "underline"),
)
nueva_localidad = StringVar()
localidad_e = Entry(frame_datos, textvariable=nueva_localidad, width=25, font=10)

cod_postal = Label(
    frame_datos,
    text="Codigo postal",
    fg="#091540",
    font=("Helvetica", 11, "bold", "underline"),
)
nuevo_cod_postal = StringVar()
cod_postal_e = Entry(frame_datos, textvariable=nuevo_cod_postal, width=25, font=10)

nombre.grid(column=0, row=0, padx=10, pady=10, columnspan=1)
nombre_e.grid(column=1, row=0, padx=15, pady=15)

apellido.grid(column=2, row=0, padx=10, pady=10)
apellido_e.grid(column=3, row=0, padx=10)

telefono.grid(column=0, row=3, padx=10, pady=10)
telefono_e.grid(column=1, row=3)

correo.grid(column=2, row=3, padx=10, pady=10)
correo_e.grid(column=3, row=3)

documento.grid(column=0, row=5, padx=10, pady=10)
documento_e.grid(column=1, row=5)

localidad.grid(column=2, row=5, padx=10, pady=10)
localidad_e.grid(column=3, row=5)

direccion.grid(column=0, row=7, padx=10, pady=10)
direccion_e.grid(column=1, row=7, pady=10)

cod_postal.grid(column=2, row=7, padx=10, pady=10)
cod_postal_e.grid(column=3, row=7)

# Deshabilitando los entrys
nombre_e.configure(state="disabled")
apellido_e.configure(state="disabled")
telefono_e.configure(state="disabled")
correo_e.configure(state="disabled")
documento_e.configure(state="disabled")
localidad_e.configure(state="disabled")
direccion_e.configure(state="disabled")
cod_postal_e.configure(state="disabled")


def mostrar_datos():
    # Habilitando los entrys
    error = False
    try:
        selection = tree.selection()[0]
    except:
        messagebox.showerror("Error", "Primero seleccione un cliente.")
        error = True
    if not error:
        nombre_e.configure(state="normal")
        apellido_e.configure(state="normal")
        telefono_e.configure(state="normal")
        correo_e.configure(state="normal")
        documento_e.configure(state="normal")
        localidad_e.configure(state="normal")
        direccion_e.configure(state="normal")
        cod_postal_e.configure(state="normal")
        try:
            if not encontrado:
                selection = tree.selection()[0]
                selection = int(selection)
            else:
                selection = int(indice_dni)
        except:
            selection = tree.selection()[0]
            selection = int(selection)

        dato_reemplazar = dato[selection]

        dato_a_mostrar = dato_reemplazar.split()

        # Mostrando datos existentes
        nombre_var = dato_a_mostrar[0]
        apellido_var = dato_a_mostrar[1]
        telefono_var = dato_a_mostrar[2]
        correo_var = dato_a_mostrar[3]
        documento_var = dato_a_mostrar[4]
        direccion_var = dato_a_mostrar[6].replace(".", " ")
        localidad_var = dato_a_mostrar[5].replace(".", " ")
        cp_var = dato_a_mostrar[-1]

        # Reiniciando entry
        nombre_e.delete("0", END)
        apellido_e.delete("0", END)
        documento_e.delete("0", END)
        direccion_e.delete("0", END)
        telefono_e.delete("0", END)
        correo_e.delete("0", END)
        cod_postal_e.delete("0", END)
        localidad_e.delete("0", END)

        # Mostrando nombre
        nombre_e.insert(0, nombre_var)

        # Mostrando apellidos
        apellido_e.insert("0", apellido_var)

        # Mostrando telefono
        telefono_e.insert("0", telefono_var)

        # Mostrando correo

        correo_e.insert("0", correo_var)

        # Mostrando documento
        documento_e.insert("0", documento_var)

        # Mostrando direccion
        direccion_e.insert("0", direccion_var)

        localidad_e.insert("0", localidad_var)

        cod_postal_e.insert("0", cp_var)

        def borrar(selection, nombre, apellido, btn):
            respuesta = messagebox.askokcancel(
                "¿Seguro?",
                f"¿Seguro que quiere eliminar el cliente {nombre + ' ' + apellido}?",
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
                    nombre_e.delete("0", END)
                    apellido_e.delete("0", END)
                    documento_e.delete("0", END)
                    direccion_e.delete("0", END)
                    telefono_e.delete("0", END)
                    correo_e.delete("0", END)
                    cod_postal_e.delete("0", END)
                    localidad_e.delete("0", END)

                    nombre_e.configure(state="disabled")
                    apellido_e.configure(state="disabled")
                    telefono_e.configure(state="disabled")
                    correo_e.configure(state="disabled")
                    documento_e.configure(state="disabled")
                    localidad_e.configure(state="disabled")
                    direccion_e.configure(state="disabled")
                    cod_postal_e.configure(state="disabled")
                    btn.destroy()
                    btn_guardar.destroy()
                    render_clientes()

                except IndexError:
                    pass
            else:
                pass

        eliminar_cliente_btn = Button(
            frame_datos,
            text="Eliminar cliente",
            font=("Helvetica", 10, "bold"),
            fg="red",
            command=lambda: borrar(
                selection, nombre_var, apellido_var, eliminar_cliente_btn
            ),
        )
        eliminar_cliente_btn.grid(column=4, row=5)

        def guardar():
            global cont_guardado
            dato_nombre = nuevo_nombre.get()
            dato_apellido = nuevo_apellido.get()
            dato_correo = nuevo_correo.get()
            dato_documento = nuevo_documento.get()
            dato_codigop = nuevo_cod_postal.get()
            dato_telefono = nuevo_telefono.get()
            dato_localidad = nueva_localidad.get()
            dato_direccion = nueva_direccion.get()
            if (
                dato_nombre == nombre_var
                and dato_apellido == apellido_var
                and dato_correo == correo_var
                and dato_documento == documento_var
                and dato_codigop == cp_var
                and dato_telefono == telefono_var
                and dato_localidad == localidad_var
                and dato_direccion == direccion_var
            ):
                nombre_e.delete(0, "end")
                apellido_e.delete(0, "end")
                telefono_e.delete(0, "end")
                correo_e.delete(0, "end")
                documento_e.delete(0, "end")
                localidad_e.delete(0, "end")
                direccion_e.delete(0, "end")
                cod_postal_e.delete(0, "end")
                nombre_e.configure(state="disabled")
                apellido_e.configure(state="disabled")
                telefono_e.configure(state="disabled")
                correo_e.configure(state="disabled")
                documento_e.configure(state="disabled")
                localidad_e.configure(state="disabled")
                direccion_e.configure(state="disabled")
                cod_postal_e.configure(state="disabled")
                btn_guardar.destroy()
                eliminar_cliente_btn.destroy()

            else:
                if dato_nombre != nombre_var:
                    editar(selection, nombre_var, dato_nombre)
                elif dato_apellido != apellido_var:
                    editar(
                        selection,
                        apellido_var,
                        dato_apellido,
                    )
                elif dato_correo != correo_var:
                    editar(
                        selection,
                        correo_var,
                        dato_correo,
                    )
                elif dato_documento != documento_var:
                    editar(
                        selection,
                        documento_var,
                        dato_documento,
                    )
                elif dato_codigop != cp_var:
                    editar(
                        selection,
                        cp_var,
                        dato_codigop,
                    )
                elif dato_telefono != telefono_var:
                    editar(
                        selection,
                        telefono_var,
                        dato_telefono,
                    )
                elif dato_localidad != localidad_var:
                    editar(
                        selection,
                        localidad_var,
                        dato_localidad,
                    )
                elif dato_direccion != direccion_var:
                    editar(
                        selection,
                        direccion_var,
                        dato_direccion,
                    )
            messagebox.showinfo(
                "Guardado", "Cambios realizados en el cliente guardado correctamente"
            )
            # Actualizo nuevamente la lista de los clientes
            render_clientes()
            # Vaciando entrys
            nombre_e.delete(0, "end")
            apellido_e.delete(0, "end")
            telefono_e.delete(0, "end")
            correo_e.delete(0, "end")
            documento_e.delete(0, "end")
            localidad_e.delete(0, "end")
            direccion_e.delete(0, "end")
            cod_postal_e.delete(0, "end")
            nombre_e.configure(state="disabled")
            apellido_e.configure(state="disabled")
            telefono_e.configure(state="disabled")
            correo_e.configure(state="disabled")
            documento_e.configure(state="disabled")
            localidad_e.configure(state="disabled")
            direccion_e.configure(state="disabled")
            cod_postal_e.configure(state="disabled")
            btn_guardar.destroy()
            eliminar_cliente_btn.destroy()

        btn_guardar = Button(
            frame_datos,
            text="Guardar cambios",
            command=guardar,
            font=("Helvetica", 9, "bold"),
        )
        btn_guardar.grid(column=4, row=3)


mostrar_datos_btn = Button(
    frame_datos,
    text="Mostrar datos",
    command=mostrar_datos,
    font=("Helvetica", 9, "bold"),
)
mostrar_datos_btn.grid(row=0, column=4, padx=20)

counter = 0

# Agregando clientes al treeview
def render_clientes():
    global dato
    global count
    count = 0
    tree.delete(*tree.get_children())
    f = open("assets/txt/clientes.txt", "r")
    dato = f.read().split(",")
    if dato != []:
        for x in range(len(dato) - 1):
            dato_split = dato[x].split()
            if "." in dato_split[5]:
                dato_split[5] = dato_split[5].replace(".", " ")
            if "." in dato_split[6]:
                dato_split[6] = dato_split[6].replace(".", " ")
            tree.insert(
                "",
                END,
                id=count,
                values=(
                    dato_split[0],
                    dato_split[1],
                    dato_split[2],
                    dato_split[3],
                    dato_split[4],
                    dato_split[5],
                    dato_split[6],
                    dato_split[-1],
                ),
            )
            count += 1
            dato_split = []


render_clientes()


# Creando boton para agregar cliente
agregar_cliente_btn = Button(
    tree_frame,
    text="Agregar cliente",
    font=("Helvetica", 10, "bold", "underline"),
    command=agregar_cliente,
)

agregar_cliente_btn.grid(column=2, row=1, padx=5, sticky=NW)
agregar_cliente_btn.place(x=10, y=295)

# Buscador de clientes
buscador_label = Label(
    tree_frame,
    text="Buscar cliente por DNI",
    font=("Helvetica", 10, "bold"),
)
buscador_label.grid(column=2, row=1, sticky=NW, padx=5)
buscador_label.place(x=140, y=300)

dni_val = StringVar()
buscador_entry = Entry(
    tree_frame, textvariable=dni_val, width=20, font=("Helvetica", 10)
)
buscador_entry.grid(column=2, row=1, padx=5, sticky=NW)
buscador_entry.place(x=300, y=300)


def renderizar_busqueda():
    global dato
    global count
    global indice_dni
    global encontrado

    encontrado = False
    dni_valor = dni_val.get()
    count = 0
    tree.delete(*tree.get_children())
    f = open("assets/txt/clientes.txt", "r")
    dato = f.read().split(",")
    if dato != []:
        for x in range(len(dato) - 1):
            dato_split = dato[x].split()
            if "." in dato_split[5]:
                dato_split[5] = dato_split[5].replace(".", " ")
            if "." in dato_split[6]:
                dato_split[6] = dato_split[6].replace(".", " ")

            if dato_split[4] == dni_valor:
                indice_dni = x
                encontrado = True
                tree.insert(
                    "",
                    END,
                    id=count,
                    values=(
                        dato_split[0],
                        dato_split[1],
                        dato_split[2],
                        dato_split[3],
                        dato_split[4],
                        dato_split[5],
                        dato_split[6],
                        dato_split[-1],
                    ),
                )
                count += 1
                dato_split = []
                buscador_entry.delete(0, "end")

            elif dni_valor == "":
                encontrado = False
                tree.insert(
                    "",
                    END,
                    id=count,
                    values=(
                        dato_split[0],
                        dato_split[1],
                        dato_split[2],
                        dato_split[3],
                        dato_split[4],
                        dato_split[5],
                        dato_split[6],
                        dato_split[-1],
                    ),
                )
                count += 1
                dato_split = []

        if not encontrado and dni_valor != "":
            messagebox.showerror(
                "Error", f"Cliente con DNI: {dni_valor} no encontrado."
            )
            encontrado = False
            buscador_entry.delete(0, "end")
            render_clientes()

        def mostrar_todos_f():
            global dato
            global count
            global encontrado
            encontrado = False
            count = 0
            tree.delete(*tree.get_children())
            f = open("assets/txt/clientes.txt", "r")
            dato = f.read().split(",")
            if dato != []:
                for x in range(len(dato) - 1):
                    dato_split = dato[x].split()
                    if "." in dato_split[5]:
                        dato_split[5] = dato_split[5].replace(".", " ")
                    if "." in dato_split[6]:
                        dato_split[6] = dato_split[6].replace(".", " ")
                    tree.insert(
                        "",
                        END,
                        id=count,
                        values=(
                            dato_split[0],
                            dato_split[1],
                            dato_split[2],
                            dato_split[3],
                            dato_split[4],
                            dato_split[5],
                            dato_split[6],
                            dato_split[-1],
                        ),
                    )
                    count += 1
                    dato_split = []

    if dni_valor != "" and encontrado:
        mostrar_todos_btn = Button(
            tree_frame,
            text="Mostrar todos",
            font=("Helvetica", 10, "bold", "underline"),
            command=mostrar_todos_f,
        )
        mostrar_todos_btn.grid(column=2, row=1, sticky=NW, padx=5)
        mostrar_todos_btn.place(x=520, y=295)


buscar_btn = Button(
    tree_frame,
    text="Buscar",
    font=("Helvetica", 10, "bold", "underline"),
    command=renderizar_busqueda,
)
buscar_btn.grid(column=2, row=1, sticky=NW, padx=5)
buscar_btn.place(x=455, y=295)

# SECCION DE PRODUCTOS ----------------
# Seccion de productos
frame_productos = LabelFrame(root, text="Productos", font=("Helvetica", 12, "bold"))
frame_productos.grid(column=0, row=2, sticky=NW, padx=15, pady=15)

frame_productos.place(x=90, y=590)

# Formulario para agregar productos

# Nombre del producto
producto_nombre = Label(
    frame_productos, text="Nombre del producto: ", font=("Helvetica", 12)
)
producto_nombre.grid(column=1, row=2, padx=5, pady=5)

producto_nombre_var = StringVar()
producto_nombre_e = Entry(
    frame_productos, textvariable=producto_nombre_var, font=("Helvetica", 11)
)
producto_nombre_e.grid(column=2, row=2, padx=10, pady=10)

# Precio del producto
producto_precio = Label(
    frame_productos, text="Precio del producto: ", font=("Helvetica", 12)
)
producto_precio.grid(column=1, row=3, padx=5, pady=5)

producto_precio_var = StringVar()
producto_precio_e = Entry(
    frame_productos, textvariable=producto_precio_var, font=("Helvetica", 11)
)
producto_precio_e.grid(column=2, row=3)

# Tipo de producto
tipo_producto = Label(frame_productos, text="Tipo: ", font=("Helvetica", 12))
tipo_producto.grid(column=1, row=4, padx=5, pady=5)

tipos = ["Lubricantes", "Combustibles"]
tipo_producto_var = StringVar()
tipo_producto_var.set("Seleccione un tipo")

tipo_producto_drop = OptionMenu(frame_productos, tipo_producto_var, *tipos)
tipo_producto_drop.grid(column=2, row=4, padx=10, pady=10, ipadx=12)


def agregar_producto_message(**args):
    nombre_producto, precio_producto, tipo_producto_get = (
        producto_nombre_var.get(),
        producto_precio_var.get(),
        tipo_producto_var.get(),
    )
    tipo_producto_prefix = "L" if tipo_producto_get == "Lubricantes" else "C"

    if (
        not nombre_producto
        or not precio_producto
        or tipo_producto_get == "Seleccione un tipo"
    ):
        messagebox.showerror("Error", "Los campos son obligatorios.")

    else:
        pregunta = messagebox.askyesno(
            "Agregar",
            f"¿Seguro que quiere agregar el producto {nombre_producto} cuyo precio es ${precio_producto}?",
        )
        if pregunta:
            agregar_producto(nombre_producto, precio_producto, tipo_producto_prefix)
            messagebox.showinfo("Agregado", "Producto agregado con exito.")
            producto_nombre_e.delete("0", END)
            producto_precio_e.delete("0", END)
            producto_nombre_e.focus()


# Boton para agregar
producto_agregar_btn = Button(
    frame_productos,
    text="Agregar producto",
    font=("Helvetica", 11),
    command=agregar_producto_message,
)
producto_agregar_btn.grid(column=3, row=2, padx=10, pady=10)

# SECCION DE VISTA DE PRODUCTOS
# Funcion para ver los productos


def ver_productos():
    global lista_productos, count_id_productos
    # Creando top
    top_productos = Toplevel()
    top_productos.title("Lista de productos")
    top_productos.resizable(0, 0)

    tree_productos = ttk.Treeview(top_productos)
    tree_productos.grid(column=2, row=0)

    tree_productos["columns"] = ("Nombre", "Precio", "Tipo")

    tree_productos.column("#0", stretch=NO, width=0)
    tree_productos.column("Nombre", width=160, anchor=N)
    tree_productos.column("Precio", width=100, anchor=N)
    tree_productos.column("Tipo", width=120, anchor=N)

    tree_productos.heading("#0")
    tree_productos.heading("Nombre", text="Nombre")
    tree_productos.heading("Precio", text="Precio")
    tree_productos.heading("Tipo", text="Tipo")

    def eliminar_tree_productos():
        selec = tree_productos.selection()[0]
        tree_productos.delete(selec)

    count_id_productos = 0
    # Renderizando productos
    tree_productos.delete(*tree_productos.get_children())
    f = open("assets/txt/productos.txt", "r")
    dato_productos = f.read().split(",")
    lista_productos = []

    if dato_productos != []:
        for x in range(len(dato_productos) - 1):
            dato_productos_split = dato_productos[x].split()
            tipo_prod = (
                "Combustible" if dato_productos_split[2] == "C" else "Lubricante"
            )
            if "." in dato_productos_split[0]:
                dato_productos_split[0] = dato_productos_split[0].replace(".", " ")

            tree_productos.insert(
                "",
                END,
                id=count_id_productos,
                values=(
                    dato_productos_split[0],
                    dato_productos_split[1],
                    tipo_prod,
                ),
            )
            lista_productos.append(dato_productos_split[0])
            count_id_productos += 1
            dato_productos_split = []

    # Creando funcion para eliminar productos
    def eliminar_producto():
        selection_producto = tree_productos.selection()[0]
        borrar_producto(
            selection_producto,
            top_productos,
            eliminar_tree_productos,
        )

    btn_eliminar_producto = Button(
        top_productos,
        text="Eliminar producto",
        font=("Helvetica", 11, "bold"),
        command=eliminar_producto,
    )
    btn_eliminar_producto.grid(column=2, row=3, padx=10, pady=10)
    top_productos.mainloop()


ver_productos_btn = Button(
    frame_productos,
    text="Ver productos",
    font=("Helvetioca", 11),
    command=ver_productos,
)
ver_productos_btn.grid(column=3, row=3, padx=10, pady=10, ipadx=10)

# Zona de ticket
ticket_label = LabelFrame(root, text="Ticket", font=("Helvetica", 12, "bold"))
ticket_label.grid(column=2, row=2, sticky=NW, pady=15, padx=15)
ticket_label.place(x=650, y=590)

# Nombre
nombre_ticket = Label(ticket_label, text="Nombre", font=("Helvetica", 12, "bold"))
nombre_ticket.grid(column=0, row=0, padx=5, pady=10)

nombre_ticket_e = Entry(ticket_label, font=("Helvetica", 11))
nombre_ticket_e.grid(column=1, row=0, padx=10, pady=10)

# Apellido
apellido_ticket = Label(ticket_label, text="Apellido", font=("Helvetica", 12, "bold"))
apellido_ticket.grid(column=0, row=1, padx=5, pady=10)
apellido_ticket_e = Entry(ticket_label, font=("Helvetica", 11))
apellido_ticket_e.grid(column=1, row=1, padx=10, pady=10)

# Direccion
direccion_ticket = Label(ticket_label, text="Direccion", font=("Helvetica", 12, "bold"))
direccion_ticket.grid(column=2, row=0, padx=5, pady=5)
direccion_ticket_e = Entry(ticket_label, font=("Helvetica", 11))
direccion_ticket_e.grid(column=3, row=0, padx=10, pady=10)

# Localidad
localidad_ticket = Label(ticket_label, text="Localidad", font=("Helvetica", 12, "bold"))
localidad_ticket.grid(column=2, row=1, padx=5, pady=5)
localidad_ticket_e = Entry(ticket_label, font=("Helvetica", 11))
localidad_ticket_e.grid(column=3, row=1, padx=10, pady=10)

# Deshabilitando la escritura de los botones
def deshabilitar_btn():
    nombre_ticket_e.configure(state="disabled")
    apellido_ticket_e.configure(state="disabled")
    direccion_ticket_e.configure(state="disabled")
    localidad_ticket_e.configure(state="disabled")


def habilitar_btn():
    nombre_ticket_e.configure(state="normal")
    apellido_ticket_e.configure(state="normal")
    direccion_ticket_e.configure(state="normal")
    localidad_ticket_e.configure(state="normal")


def reiniciar_entrys():
    nombre_ticket_e.delete("0", END)
    apellido_ticket_e.delete("0", END)
    direccion_ticket_e.delete("0", END)
    localidad_ticket_e.delete("0", END)


deshabilitar_btn()

# Cargar datos
def cargar_datos():
    habilitar_btn()
    reiniciar_entrys()
    deshabilitar_btn()

    try:
        if not encontrado:
            ticket_selection = tree.selection()[0]
            ticket_selection = int(ticket_selection)
        else:
            ticket_selection = int(indice_dni)
    except:
        ticket_selection = tree.selection()[0]
        ticket_selection = int(ticket_selection)

    f = open("assets/txt/clientes.txt", "r")
    dato = f.read().split(",")
    dato_selection = dato[ticket_selection].split()
    if dato_selection != []:
        for x in range(len(dato_selection) - 1):
            if "." in dato_selection[5]:
                dato_selection[5] = dato_selection[5].replace(".", " ")
            if "." in dato_selection[6]:
                dato_selection[6] = dato_selection[6].replace(".", " ")
        nombre, apellido, direccion, localidad = (
            dato_selection[0],
            dato_selection[1],
            dato_selection[6],
            dato_selection[5],
        )
        habilitar_btn()
        nombre_ticket_e.insert("0", nombre)
        apellido_ticket_e.insert("0", apellido)
        direccion_ticket_e.insert("0", direccion)
        localidad_ticket_e.insert("0", localidad)
        deshabilitar_btn()

        def info_ticket():
            top_ticket = Toplevel()
            top_ticket.title("Informacion del ticket")
            top_ticket.resizable(0, 0)

            # DATOS PARA EL OPTIONMENU
            f = open("assets/txt/productos.txt", "r")
            dato_productos = f.read().split(",")
            lista_productos = []
            lista_precios = []
            if dato_productos != []:
                for x in range(len(dato_productos) - 1):
                    dato_productos_split = dato_productos[x].split()
                    if "." in dato_productos_split[0]:
                        dato_productos_split[0] = dato_productos_split[0].replace(
                            ".", " "
                        )
                    lista_productos.append(dato_productos_split[0])
                    lista_precios.append(dato_productos_split[1])
                    dato_productos_split = []
                f.close()

            producto = Label(top_ticket, text="Producto", font=("Helvetica", 12))
            producto.grid(column=0, row=0, padx=10, pady=10)

            cantidad_producto = Label(
                top_ticket,
                text="Cantidad del producto",
                font=("Helvetica", 12),
                padx=10,
                pady=10,
            )
            cantidad_producto.grid(column=0, row=1)
            cantidad_producto_var = IntVar()
            cantidad_producto_e = Entry(
                top_ticket, textvariable=cantidad_producto_var, font=("Helvetica", 11)
            )
            cantidad_producto_e.grid(column=1, row=1, padx=10, pady=10)

            value = StringVar()
            value.set("Elija un producto")
            drop = OptionMenu(top_ticket, value, *lista_productos)
            drop.grid(column=1, row=0, padx=10, pady=10)

            # Preguntando forma de pago
            formas_de_pago = ["Efectivo", "Codigo QR", "Credito"]
            forma_de_pago_label = Label(
                top_ticket, text="Forma de pago", font=("Helvetica", 12)
            )
            forma_de_pago_label.grid(column=0, row=2)
            forma_de_pago_var = StringVar()
            forma_de_pago_var.set("Seleccione forma de pago")
            option_menu_formapago = OptionMenu(
                top_ticket, forma_de_pago_var, *formas_de_pago
            )
            option_menu_formapago.grid(column=1, row=2, padx=10, pady=10)

            # Colocando fecha
            fecha_label = Label(top_ticket, text="Fecha", font=("Helvetica", 12))
            fecha_label.grid(column=0, row=3)
            fecha_e = Entry(top_ticket, font=("Helvetica", 11))
            fecha_e.grid(column=1, row=3, padx=10, pady=10)
            fecha_actual = datetime.today().strftime("%Y-%m-%d %H:%M")
            fecha_e.insert("0", fecha_actual)
            fecha_e.configure(state="disabled")

            def emitir_ticket():
                cantidad = int(cantidad_producto_var.get())
                if (
                    value.get() == "Elija un producto"
                    or forma_de_pago_var.get() == "Seleccione forma de pago"
                    or cantidad <= 0
                ):
                    messagebox.showerror("Error", "Campos incorrectos.")
                else:
                    valor = value.get()
                    index = lista_productos.index(valor)
                    precio_producto = int(lista_precios[index])
                    nombre_producto = lista_productos[index]
                    precio_total_var = precio_producto * cantidad
                    if forma_de_pago_var.get() == "Efectivo":
                        precio_total_var -= precio_total_var * 0.05

                    precio_total = Label(
                        top_ticket, text="Precio total", font=("Helvetica", 12)
                    )
                    precio_total.grid(column=0, row=4, padx=10, pady=10)
                    precio_total_e = Entry(top_ticket, font=("Helvetica", 11))
                    precio_total_e.grid(column=1, row=4, padx=10, pady=10)
                    precio_total_e.insert("0", "$" + str(precio_total_var))
                    precio_total_e.configure(state="disabled")

                    forma_pago = forma_de_pago_var.get()
                    emitir(
                        nombre,
                        apellido,
                        localidad,
                        direccion,
                        nombre_producto,
                        cantidad,
                        precio_producto,
                        precio_total_var,
                        forma_pago,
                        fecha_actual,
                    )
                    if emitir:
                        messagebox.showinfo(
                            "Ticket emitido", "Ticket emitido con exito."
                        )
                        top_ticket.destroy()

            drop_btn = Button(
                top_ticket,
                text="Emitir ticket",
                command=emitir_ticket,
                font=("Helvetica", 11),
            )
            drop_btn.grid(column=1, row=5, padx=10, pady=10)

            top_ticket.mainloop()

        # Informacion del ticket
        info_ticket_btn = Button(
            ticket_label,
            text="Info ticket",
            font=("Helvetica", 11),
            command=info_ticket,
        )
        info_ticket_btn.grid(column=4, row=1, padx=10, pady=10)


# Boton para cargar datos del ticket
btn_cargar_datos_ticket = Button(
    ticket_label, text="Cargar datos", font=("Helvetica", 11), command=cargar_datos
)
btn_cargar_datos_ticket.grid(column=4, row=0, padx=10, pady=10)

# Funcion para ver los tickets
def ver_tickets():
    top_ver_tickets = Toplevel()
    top_ver_tickets.title("Lista de tickets")
    tree_ver_tickets = ttk.Treeview(top_ver_tickets)
    tree_ver_tickets.grid(column=0, row=0)
    top_ver_tickets.resizable(0, 0)

    tree_ver_tickets["columns"] = (
        "Nombre",
        "Apellido",
        "Localidad",
        "Direccion",
        "Producto",
        "Cantidad",
        "Precio unitario",
        "Precio total",
        "Forma de pago",
        "Fecha",
    )

    tree_ver_tickets.column("#0", stretch=NO, width=0)
    tree_ver_tickets.column("Nombre", width=100, anchor=N)
    tree_ver_tickets.column("Apellido", width=100, anchor=N)
    tree_ver_tickets.column("Localidad", width=110, anchor=N)
    tree_ver_tickets.column("Direccion", width=110, anchor=N)
    tree_ver_tickets.column("Producto", width=200, anchor=N)
    tree_ver_tickets.column("Cantidad", width=70, anchor=N)
    tree_ver_tickets.column("Precio unitario", width=100, anchor=N)
    tree_ver_tickets.column("Precio total", width=100, anchor=N)
    tree_ver_tickets.column("Forma de pago", width=100, anchor=N)
    tree_ver_tickets.column("Fecha", width=100, anchor=N)

    tree_ver_tickets.heading("#0")
    tree_ver_tickets.heading("Nombre", text="Nombre")
    tree_ver_tickets.heading("Apellido", text="Apellido")
    tree_ver_tickets.heading("Localidad", text="Localidad")
    tree_ver_tickets.heading("Direccion", text="Direccion")
    tree_ver_tickets.heading("Producto", text="Producto")
    tree_ver_tickets.heading("Cantidad", text="Cantidad")
    tree_ver_tickets.heading("Precio unitario", text="Precio unitario")
    tree_ver_tickets.heading("Precio total", text="Precio total")
    tree_ver_tickets.heading("Forma de pago", text="Forma de pago")
    tree_ver_tickets.heading("Fecha", text="Fecha")

    archivo_tickets = open("assets/txt/tickets.txt", "r")
    dato_tickets = archivo_tickets.read().split(",")
    try:
        if dato_tickets != []:
            for x in range(len(dato_tickets)):
                dato_split = dato_tickets[x].split()
                if "." in dato_split[2]:
                    dato_split[2] = dato_split[2].replace(".", " ")
                if "." in dato_split[3]:
                    dato_split[3] = dato_split[3].replace(".", " ")
                if "." in dato_split[4]:
                    dato_split[4] = dato_split[4].replace(".", " ")
                if len(dato_split) == 12:
                    tree_ver_tickets.insert(
                        "",
                        END,
                        values=(
                            dato_split[0],
                            dato_split[1],
                            dato_split[2],
                            dato_split[3],
                            dato_split[4],
                            dato_split[5],
                            dato_split[6],
                            dato_split[7],
                            dato_split[8] + " " + dato_split[9],
                            dato_split[10:],
                        ),
                    )
                else:
                    tree_ver_tickets.insert(
                        "",
                        END,
                        values=(
                            dato_split[0],
                            dato_split[1],
                            dato_split[2],
                            dato_split[3],
                            dato_split[4],
                            dato_split[5],
                            dato_split[6],
                            dato_split[7],
                            dato_split[8],
                            dato_split[9:],
                        ),
                    )
                dato_split = []
    except:
        pass
    top_ver_tickets.mainloop()


# Boton para ver tickets
ver_tickets_btn = Button(
    ticket_label, text="Ver tickets", font=("Helvetica", 11), command=ver_tickets
)
ver_tickets_btn.grid(column=5, row=0, padx=10, pady=10)

root.iconbitmap("assets/img/icono.ico")
root.mainloop()
