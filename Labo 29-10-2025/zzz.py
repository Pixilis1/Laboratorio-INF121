

import tkinter as tk
from cProfile import label
from tkinter import filedialog
ventana = tk.Tk()
ventana.title("Bloc zzz")
ventana.geometry("800x600")

menu = tk.Menu(ventana)
ventana.config(menu=menu)

archivo = tk.Menu(menu)
menu.add_cascade(label="GGGG",menu=archivo)
editar = tk.Menu(menu)
menu.add_cascade(label="Editar",menu=archivo)

def mostrarMultiplicacion():
    nro1=int(entry.get())
    nro2=int(entryy.get())
    resultado=nro1*nro2
    resultado1=nro1+nro2
    resultado2 = nro1 - nro2
    resultado3 = nro1 / nro2
    resultadoText.config(text=f"Resultado:{resultado}")
    resultadoText1.config(text=f"Resultado1:{resultado1}")
    resultadoText2.config(text=f"Resultado2:{resultado2}")
    resultadoText3.config(text=f"Resultado3:{resultado3}")

    print(resultado)

#Entrada del nro
entry=tk.Entry(ventana)
entry.grid(row=0,column=0,padx=10,pady=20)
entryy=tk.Entry(ventana)
entryy.grid(row=0,column=1,padx=10,pady=20)

#Crear un boton
bttn=tk.Button(ventana,text="Mostrar operaciones",command=mostrarMultiplicacion)
bttn.grid(row=2,column=0,padx=10,pady=20)

#Resultado Label
resultadoText=tk.Label(ventana,text="Resultado Multiplicacion:")
resultadoText.grid(row=0,column=4,padx=10,pady=20)

resultadoText1=tk.Label(ventana,text="Resultado Suma:")
resultadoText1.grid(row=1,column=4,padx=10,pady=20)

resultadoText2=tk.Label(ventana,text="Resultado Resta:")
resultadoText2.grid(row=2,column=4,padx=10,pady=20)

resultadoText3=tk.Label(ventana,text="Resultado Division")
resultadoText3.grid(row=3,column=4,padx=10,pady=20)



ventana.mainloop()