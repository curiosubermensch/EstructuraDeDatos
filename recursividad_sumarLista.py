#sumar los elementos de una lista recursivamente
 
l=[1,2,3,4]

#mi solucion
def suma(l,i):
	if -i==-len(l):
		return l[i]
	else:
		l[-i-2]=l[-i-2]+l[-i-1]
		return suma(l,-i+1)
#######################################################################################################
#solucion simple: Suma de los elementos de una lista con ciclo for
def sumaFor(l):
	suma=0
	for i in range(len(l)):
		suma=suma+l[i]
	return suma

#####################################################################################################
#tip: usar operador que segmenta la lista e ir sumando sublistas cada vez mas pequeñas hasta llegar a una lista vacía

def sumalista(l,i):
	#la hice yo pero no tengo claro como funciona :s
	if l==[]:
		return 0
	else:
		return l[i]+sumalista(l[i+1:],i)
#######################################################################################################
def sumaListaTrue(l):
	if l==[]:
		print("caso base encontrado l=[]")
		suma = 0
	else:
		print(l[0],"+",l[1:])
		suma=l[0]+sumaListaTrue(l[1:])
		print("saliendo recursion y haciendo calculo: ",suma)
	return suma
""" output:
1 + [2, 3, 4]
2 + [3, 4]
3 + [4]
4 + []
caso base encontrado l=[]
saliendo recursion y haciendo calculo:  4
saliendo recursion y haciendo calculo:  7
saliendo recursion y haciendo calculo:  9
saliendo recursion y haciendo calculo:  10
10
"""
def sumaLista(l):
	if l==[]:
		return 0
	else:
		return l[0]+sumaLista(l[1:])

print(sumaLista(l))