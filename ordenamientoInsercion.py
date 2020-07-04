#Ordenamiento por insercion (baraja de cartas en escala [de menor a mayor])

#1. partir evaluando POSICION hacia adelante siempre.
#2. si a la izquierda el numero es mayor hay que intercambiar para ordenar el array.

#En otras palabras:

#1. Recorremos cada elemento del array.
#2. Cada elemento del array se ordena: Si a su izquierda tiene un elemento MAYOR que el entonces los intercambiamos de sitio. Se mueve a la izquierda tantas veces como sea necesario para cumplir con que el de la izquierda sea menor o llegue al limite izquierdo.

#==================================consideraciones=======================================

#1. La flecha que recorre cada posicion:
	#Se convierte en un bucle for (principal)

#2. El elemento que se mueve a la izquierda:
	#Necesitamos recordar en una variable cual es la posicion del elemento q esta siendo ordenado segun se mueve
#==============================================================================================================

def insercionSimple():
	#del video de makigas:
	#version menos eficiente
	lista=[6,4,2,1,3,5]
	for i in range(1,len(lista)): #"i" representa la flecha q recorre el array de izq a derecha sin retroceder
		pos=i #posicion del evaluando a ordenar
		#el while ira moviendo tantas veces sea necesario el evaluando para ordenarlo
		while pos>=1 and lista[pos-1]>lista[pos]: #que sea el segundo elemento (o mas) y si el de la izquierda es mayor que el evaluando entonces hacer el cambiazo
			#estos intercambios son los ineficientes:
			aux=lista[pos-1]  #guardamos el de la izq en una variable auxiliar
			lista[pos-1]=lista[pos] #el de la izq toma la posicion que tenia el evaluando a ordenar
			lista[pos]=aux #el evaluando a ordenar (q es menor) pasa a ser el de la izquierda q era mayor, osea q queda ordenado el arreglo de menor a mayor 
			pos=pos-1 #para que en la sgte vuelta de while se evalue si el nuevo vecino de la izquierda es mayor q el evaluando, asi todos los elementos que estan a la izquierda de la flecha seran evaluados y ordenados de ser necesario 
			print(lista)
#output:
# [4, 6, 2, 1, 3, 5]
# [4, 2, 6, 1, 3, 5]
# [2, 4, 6, 1, 3, 5]
# [2, 4, 1, 6, 3, 5]
# [2, 1, 4, 6, 3, 5]
# [1, 2, 4, 6, 3, 5]
# [1, 2, 4, 3, 6, 5]
# [1, 2, 3, 4, 6, 5]
# [1, 2, 3, 4, 5, 6]

def insercionEficiente():
	#para que no haga cambios innecesarios sino q lo setee solo cuando corresponde, osea de golpe lo ordena como en el gif:
	lista=[6,4,2,1,3,5]
	for i in range(1,len(lista)): #"i" representa la flecha q recorre el array de izq a derecha sin retroceder
		pos=i #posicion del evaluando a ordenar
		valor=lista[i] #guardamos el valor evaluando en una variable para cambiarla 1 sola vez luego del while
		#el while ira moviendo tantas veces sea necesario el evaluando para dejarlo ordenado a la izq
		while pos>=1 and lista[pos-1]>valor: #que sea el 2do elemento y si el de la izq es mayor q nuestro evaluando
			lista[pos]=lista[pos-1] #pasamos el mayor a la posicion evaluando, desplazamiento a la derecha
			pos=pos-1 #para que siga evaluando a la izquierda
			print(lista)
		#luego de que se haya seteado la posicion de la flecha con el mayor, seteamos la posicion del menor:
		lista[pos]=valor #reescribimos el evaluando que estaba en la flecha en su nueva posicion quedando ordenado 
		#print(lista)
#output:
# [4, 6, 2, 1, 3, 5]
# [2, 4, 6, 1, 3, 5]
# [1, 2, 4, 6, 3, 5]
# [1, 2, 3, 4, 6, 5]
# [1, 2, 3, 4, 5, 6]
insercionEficiente()


def miOrdInsercion():
	#este lo hice yo
	lista=[6,4,2,1,3,5]
	print(lista)
	for i in range(1,len(lista)):
		for j in range(len(lista[0:i])):
			if lista[j]>lista[i]:
				aux=lista[i]
				lista[i]=lista[j]
				lista[j]=aux
			print(lista)
#output:
# [6, 4, 2, 1, 3, 5]
# [4, 6, 2, 1, 3, 5]
# [2, 6, 4, 1, 3, 5]
# [2, 4, 6, 1, 3, 5]
# [1, 4, 6, 2, 3, 5]
# [1, 2, 6, 4, 3, 5]
# [1, 2, 4, 6, 3, 5]
# [1, 2, 4, 6, 3, 5]
# [1, 2, 4, 6, 3, 5]
# [1, 2, 3, 6, 4, 5]
# [1, 2, 3, 4, 6, 5]
# [1, 2, 3, 4, 6, 5]
# [1, 2, 3, 4, 6, 5]
# [1, 2, 3, 4, 6, 5]
# [1, 2, 3, 4, 6, 5]
# [1, 2, 3, 4, 5, 6]



#insercionSimple()
#ankiar "que ordenamiento hace este?"
def insercion2():
	#el de cesar ramos [curso ED python]:
	lista=[6,4,2,1,3,5]
	for i in range(1,len(lista)):
		aux=lista[i] #el elemento actual
		j=i-1#variable q ira decrementando a la izq, comparar el elemento actual con el de la izq
		while j>=0 and aux<lista[j]:
			lista[j+1]=lista[j]
			lista[j]=aux
			j-=1
			print(lista)
#output:
# [4, 6, 2, 1, 3, 5]
# [4, 2, 6, 1, 3, 5]
# [2, 4, 6, 1, 3, 5]
# [2, 4, 1, 6, 3, 5]
# [2, 1, 4, 6, 3, 5]
# [1, 2, 4, 6, 3, 5]
# [1, 2, 4, 3, 6, 5]
# [1, 2, 3, 4, 6, 5]
# [1, 2, 3, 4, 5, 6]
def insercionMaster():
	#del video de masterhehegar
	lista=[6,4,2,1,3,5]
	for i in range(1,len(lista)):
		pass


