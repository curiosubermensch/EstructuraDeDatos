from nodo import Nodo #importamos la clase nodo

#un nodo contiene dos atributos: "dato" (item) y "siguiente" (otro nodo o None)

class ListaSimpleEnlazada():

	def __init__(self):
		self.primero = None #nodo cabeza
		self.ultimo = None #nodo cola

	# def vacia(self): # no creo que está bien
	# 	return self.primero == None

	def vacia(self):
		if self.primero == None:
			return True
		else:
			return False

	def agregarUltimo(self, dato):
		if self.vacia():
			self.primero = self.ultimo = Nodo(dato)
		else:
			#aux = self.ultimo #guardamos en memoria el ultimo nodo
			aux=Nodo(dato)
			self.ultimo.siguiente=aux #seteamos el valor sgte del ultimo nodo con el agregado
			self.ultimo=aux #seteamos el ultimo nodo con el agregado nuevo
			#self.ultimo = aux.siguiente=Nodo(dato) #una manera mas corta de hacerlo 
	
	def agregarInicio(self, dato):
		if self.vacia():
			self.primero = self.ultimo = Nodo(dato)
		else:
			aux=self.primero #guardo el primero
			self.primero = Nodo(dato) #creo el nuevo nodo en el primero
			self.primero.siguiente = aux #transformo el ATRIBUTO del (ex)primero en siguiente
			

	def eliminaInicio(self):
		self.primero = self.primero.siguiente



	def eliminaUltimo(self):
		#hay que recorrer la lista pa saber cual es el ultimo
		aux=self.primero
		while aux.siguiente != self.ultimo: #termina cuando aux.siguiente == self.ultimo
			aux=aux.siguiente
		aux.siguiente=None #como ya llegamos al penultimo nos pitiamos el ultimo
		self.ultimo=aux #ahora el ultimo es aux que a su vez es el penultimo


	def recorreImprime(self):
		aux=self.primero
		while aux != None:
			print(aux.dato, end=" ") #accedemos a lo que tiene adentro el nodo
			aux=aux.siguiente #para acceder al sgte nodo
		print()
