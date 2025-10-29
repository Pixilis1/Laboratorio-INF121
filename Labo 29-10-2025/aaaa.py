
import tkinter as tk
from datetime import datetime

def crear_ventana_menu():
    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Menu")
    ventana.geometry("300x150")
    ventana.configure(bg='pink')
    frame=tk.Frame(ventana)
    frame1=tk.Frame(ventana)

    # Configurar la fecha actual (o la fecha específica que quieras)
    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
    # Si quieres usar la fecha específica del ejemplo:
    # fecha_actual = "29/10/2025 09:21"

    # Etiqueta del título "Menu"
    lbl_titulo = tk.Label(
        ventana,
        text="Menu",
        font=("Arial", 16, "bold"),
        bg='white',
        fg='black'
    )
    lbl_titulo.pack(pady=20)

    # Etiqueta de fecha y hora
    lbl_fecha = tk.Label(
        ventana,
        text=fecha_actual,
        font=("Arial", 12),
        bg='beige',
        fg='black'
    )
    lbl_fecha.pack(pady=10)

    return ventana


# Crear y ejecutar la ventana
if __name__ == "__main__":
    app = crear_ventana_menu()
    app.mainloop()