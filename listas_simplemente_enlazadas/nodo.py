#Lista simplemente enlazada

#> A diferencia de los arrays para acceder a los elementos de una lista enlaza se debe hacer mediante un PUNTERO

#> Posee 1 enlace por nodo el cual apunta al sgte en la lista o a null/None si es que es el ultimo

class Nodo():
	
	def __init__(self, dato):
		self.dato=dato
		self.siguiente=None #apunta a nulo