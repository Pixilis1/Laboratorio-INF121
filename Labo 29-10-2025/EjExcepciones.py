
import math
from multiprocessing.managers import Array


#class EjExcepciones:
 #   def __init__(self):

class main:
    a=9
    b=3
    try:
        c = a / b
        print(c)
    except ArithmeticError as e:
        print("Divison entre 0")

x=-1
try:
    raiz = math.sqrt(x)
    print(raiz)
except ValueError as e:
    print("No existe raiz de un nro negativo")


u=[1,2,3]

try:
    print(u[5])
except IndexError as e:
    print("Indice fuera de rango")