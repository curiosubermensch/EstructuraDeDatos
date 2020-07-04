#ordenamiento por seleccion:
#buscar el elemento más pequeño de la lista
#intercambiarlo por el actual
#seguir buscando el dato mas pequeño
#intercambiarlo por el actual
#hacer el proceso de manera sucesiva

def ordenamiento1():
	lista=[4,2,6,8,5,7,0]
	print(lista)
	menor=lista[0]
	for i in range(len(lista)):
		for j in range(len(lista)):
			if lista[i]<lista[j]:
				menor=lista[i]
				lista[i]=lista[j]
				lista[j]=menor
				print(lista)


#ordenamiento por seleccion
#usar nombres mnemotecnicos
#para las variables (3 caracteres)
lista=[4,2,6,8,5,7,0]
print(lista)
#i sera el ultimo que se esta ordenando
for i in range(len(lista)):
	min=i #suponemos q es la posicion donde se encuentra el minimo
	for j in range(i,len(lista)): ##los j seran el rango restante para encontrar el minimo
		if lista[j]<lista[min]: ##si el menor del rango es menor que el ultimo evaluando 
			min=j ##seteamos la posicion minima supuesta por la posicion del menor del rango y queda en orden
	#aqui hacemos el cambiazo:
	aux=lista[i] #auxiliar
	lista[i]=lista[min] #el elemento evaluado lo igualamos al (osea pasa a ser el) menor del rango
	lista[min]=aux ##el minimo del rango restante pasa a ser el evaluado
	print(lista)  #imprimimos cada cambiazo
#output:
# [4, 2, 6, 8, 5, 7, 0]
# [0, 2, 6, 8, 5, 7, 4]
# [0, 2, 6, 8, 5, 7, 4]
# [0, 2, 4, 8, 5, 7, 6]
# [0, 2, 4, 5, 8, 7, 6]
# [0, 2, 4, 5, 6, 7, 8] aqui ya la ordena por completo
# [0, 2, 4, 5, 6, 7, 8]
# [0, 2, 4, 5, 6, 7, 8]
