from os import system
#system("clear")

class Nodo():
	def __init__(self, dato, siguiente = None):
		self.dato=dato
		self.siguiente=siguiente

	def __str_(self):
		return str(self.dato)


def recorrer(nodo):
	while nodo != None:
		print(nodo.dato, end=" ")
		nodo=nodo.siguiente

nodo4= Nodo(40,None) #como no hay siguiente se pone None para asi evitar errores
nodo3= Nodo(30,nodo4)
nodo2= Nodo(20,nodo3)
nodo1= Nodo(10,nodo2)

#print(nodo1) #<__main__.Nodo object at 0x0000004E05D97348>
recorrer(nodo1)