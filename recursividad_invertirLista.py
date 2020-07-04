#invertir lista recursivamente
#ej: [1,2,3,4,5] ---> [5,4,3,2,1]
l=[1,2,3,4,5]
m=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
n=[1,2,3,4,5,6,7]
#invertir lista usando slice:
def a(l):
	print(l)
	print(l[-1::-1])

#invertir iterativamente:
def b(m):
	print(m)
	for i in range(len(m)-1): #eficiencia maxima
		m.insert(i,m[-1])
		m.pop()
		print(m)

#invertir recursivamente:
#ya que se puede sumar listas sin mas, hay que decrecer una y aumentar la otra
def invRecursiva(l):
	if l==[]:
		pass
	else:
		lista=l[-1]+invRecursiva(l[:-2])
		return lista


def invFor(l): #ta mala
	for i in range(len(l)-3):
		aux=l[-1]
		l[:0]=aux
		l[-1]=l[0]
	print(l)



def invierte(l):
	l2=[]
	for i in range(len(l)-3):
		l2[:0]=l[-1]
	return l2



def inv_recursiva(l):
	if l[0]==l[len(l)-1]:
		print(l)
	else:
		aux=l[0]
		l[0]=l[len(l)-1]
		invRecursiva(l[1:len(l)-1])
		print(l)

#otro intento de invertir recursivamente:
def x(l,m):
	return l+m
#conclusion: se puede sumar listas
#[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

###############################################################
"""
Hola, el caso base suele ser un caso tan sencillo que ya no hace falta hacer ninguna operación sobre él. A la hora de invertir una lista, si tenemos una lista vacía, la lista invertida es esa misma lista, o sea que ya no habría que hacer nada.
Por lo que, si tenemos una lista: lista = [1,2,3]
Lo primero que se hace es ir dividiendo la lista en el último elemento de la lista más el resto de la lista, por lo que obtendríamos: [3] + [1,2]
Luego se sigue recursivamente dividiendo la lista menos el último elemento, sacando de nuevo el último elemento de la lista que queda: [2] + [1]
Finalmente al sacar el último elemento nos queda sólo una lista vacía: [1] + []
Como hemos establecido que el caso base sea una lista vacía, ya que una lista vacía no hace falta invertirla, se llega al caso base, se sale de la recursión, y al salir de la recursión se van concatenando los trozos obtenidos en cada recursión:
[3] + [2] + [1] + [] = [3,2,1]
y obtenemos la lista inversa.
Espero que te pueda servir un poco. Un saludo.

"""

