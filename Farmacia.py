

#from multipledispatch import dispatch
class Farmacia:
    #@dispatch(str, list, list, list)
    def __init__(self,nom,medic,trabajadores,cliente):
        self.__nom=nom
        self.__medic=[]
        self.__trabajadores=[]
        self.__cliente=[]

    def getNomFarm(self):
        return self.__nom

    def agregarCliente(self,cliente):
        self.__cliente.append(cliente)
    def mostrarClientes(self):
        for cliente in self.__cliente:
            print(cliente.getNomCliente()," ",cliente.getEdad())

    def agregarMedic(self,medicamento):
        self.__medic.append(medicamento)
    def mostrarJarabes(self):
        for medicamento in self.__medic:
            if medicamento.getTipo()=="Jarabe":
                print(f"{medicamento.getNomMedic()} Vencimiento:{medicamento.getAnioVenc()} Tipo:{medicamento.getTipo()}")
    def mostrarPastillas(self):
        cont=0
        for medicamento in self.__medic:
            if medicamento.getTipo()=="Pastilla":
                print(f"{medicamento.getNomMedic()} Vencimiento:{medicamento.getAnioVenc()} Tipo:{medicamento.getTipo()}")
                cont+=medicamento.getStock()
        print("Total pastillas:",cont)

    def contarClientesEdadXY(self,edadX,edadY): #corregir
        cont=0
        for c in self.__cliente:
            if(c.edad<edadY and c.edad>edadX):
                cont+=1
        print(f"Hay {cont} clientes")
        return cont

    def mostrarStockAnioVenc(self):
        cont=0
        for medicamento in self.__medic:
            if medicamento.getAnioVenc()>=2025:
                cont+=medicamento.getStock()
        print(cont)

    #def eliminarJarabesVenc(self):

    def venderMedic(self,nomX, tipoY, cantVender):
        self.__nomX=nomX
        self.__tipoY=tipoY
        self.__cantVender=cantVender
        for medicamento in self.__medic:
            if medicamento.getNomMedic()==self.__nomX:
                if medicamento.getTipo==self.__tipoY and medicamento.getAnioVenc()>=2025:
                    medicamento.getStock()=medicamento.setStock() #Corregir
                else:
                    print("Se acabaron las unidades de ese medicamento")

            else:
                print("No tenemos ese medicamento")


class Medicamento:
    def  __init__(self,nom,anioVenc,tipo,stock):
        self.__nom=nom
        self.__anioVenc = anioVenc
        self.__tipo = tipo
        self.__stock=stock

    def getNomMedic(self):
        return self.__nom
    def getAnioVenc(self):
        return self.__anioVenc
    def getTipo(self):
        return self.__tipo
    def getStock(self):
        return self.__stock
    #def setStock(self):

class Cliente:
    def __init__(self,nom,edad):
        self.__nom=nom
        self.__edad = edad

    def getNomCliente(self):
        return self.__nom
    def getEdad(self):
        return self.__edad

cliente1=Cliente("Axel",23)
cliente2=Cliente("John",20)

medicamento1=Medicamento("Paracetamol",2025,"Pastilla",120)
medicamento2=Medicamento("Ibuprofeno",2025,"Jarabe",100)
medicamento3=Medicamento("Resfrianex",2027,"Jarabe",220)
medicamento4=Medicamento("Resfrianex",2027,"Pastilla",220)

farmacia=Farmacia("Bolivia",[],[],[])

farmacia.agregarCliente(cliente1)
farmacia.agregarCliente(cliente2)
farmacia.mostrarClientes()

farmacia.agregarMedic(medicamento1)
farmacia.agregarMedic(medicamento2)
farmacia.agregarMedic(medicamento3)
farmacia.agregarMedic(medicamento4)
farmacia.mostrarJarabes()
farmacia.mostrarPastillas()
farmacia.mostrarStockAnioVenc()

farmacia.contarClientesEdadXY(18,25)

farmacia.venderMedic("Paracetamol","Pastilla",25)
farmacia.venderMedic("Ibuprofeno","Jarabe",25)
farmacia.mostrarJarabes()
farmacia.mostrarPastillas()