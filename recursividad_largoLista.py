#definir funcion recursiva que calcule el largo de una lista


#como resolver problemas de recursividad:
#1. Definir el problema para los casos mas sencillos ej lista=[], lista=[1], n==0, lista==null 
#2. Suponemos hipotesis de que sabemos como resolverlo para cualquier x ----> largo(lista)
#3. Expresamos la solucion general del problema usando la hipotesis para un caso mas complejo que x (+1)
#----> 1+largo(l[1:])
l=[1,2,3,4,5,6,7,8]

def largo(l):
	if l==[]:
		return 0
	else:
		return 1+largo(l[1:])

print(largo(l))