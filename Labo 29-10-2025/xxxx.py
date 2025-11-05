

import tkinter as tk
from tkinter import messagebox

# Definimos las clases
class Empresa:
    def __init__(self, nom):
        self.nom = nom
        self.empleados = []

    def contratar(self, empleado):
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nom} contratado en la empresa {self.nom}")

    def listar_empleados(self):
        if len(self.empleados) == 0:
            return "Aún no hay empleados en la empresa"
        else:
            empleados_lista = ""
            for i, empleado in enumerate(self.empleados):
                empleados_lista += f"{i+1}. {empleado}\n"
            return empleados_lista


class Empleado:
    def __init__(self, nom, puesto, cDir, dDir, nDir):
        self.nom = nom
        self.puesto = puesto
        self.direccion = Direccion(cDir, dDir, nDir)

    def __str__(self):
        return f"Nombre: {self.nom} | Puesto: {self.puesto} | Dirección: {self.direccion}"

class Direccion:
    def __init__(self, ciudad, direccion, numero):
        self.ciudad = ciudad
        self.direccion = direccion
        self.numero = numero

    def __str__(self):
        return f"Ciudad: {self.ciudad} | Dirección: {self.direccion} | Número: {self.numero}"

# Funciones para la interfaz gráfica (Tkinter)
def contratar_empleado():
    nombre = entry_nombre.get()
    if nombre == "":
        messagebox.showwarning("Advertencia", "Por favor ingrese un nombre.")
        return

    # Crear un empleado con el nombre ingresado
    e = Empleado(nombre, "Junior", "La Paz", "Monoblock", 69953348)
    empresa1.contratar(e)
    entry_nombre.delete(0, tk.END)  # Limpiar el campo de entrada
    messagebox.showinfo("Contratación", f"Persona {nombre} se agrego a lalista de postulantes.")

def contratar(self,name): #Falta terminar el codigo
    for c in self.empleados:
        if name==self.empleados.nom:


def listar_empleados():
    empleados_info = empresa1.listar_empleados()
    text_empleados.delete(1.0, tk.END)  # Limpiar el área de texto
    text_empleados.insert(tk.END, empleados_info)

# Crear la ventana principal con Tkinter
ventana = tk.Tk()
ventana.title("Gestión de Empleados")
ventana.geometry("800x600")
ventana.config(bg="black")

empresa1 = Empresa("Zzzz")

# Etiqueta y caja de texto para ingresar el nombre del empleado
label_nombre = tk.Label(ventana, text="Nombre del postulante:")
label_nombre.pack(pady=10)

entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.pack(pady=5)

# Botón para contratar al empleado
btn_contratar = tk.Button(ventana, text="Postular", command=contratar_empleado)
btn_contratar.pack(pady=10)

# Botón para listar los empleados
btn_listar = tk.Button(ventana, text="Listar postulantes", command=listar_empleados)
btn_listar.pack(pady=10)

# Área de texto para mostrar la lista de empleados
text_empleados = tk.Text(ventana, height=10, width=50)
text_empleados.pack(pady=10)

label_nombre = tk.Label(ventana, text="Nombre del postulante a contratar:")
label_nombre.pack(pady=10)
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
