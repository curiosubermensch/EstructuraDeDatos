def seleccion():
	lista=[5,4,3,2,1]
	print(lista)
	for i in range(len(lista)): #i sera el ultimo que se esta ordenando
		minimo=i
		for j in range(i,len(lista)): #los j seran el rango restante para encontrar el minimo
			if lista[j]<lista[minimo]: #si el menor del rango es menor que el ultimo evaluando 
				minimo=j #seteamos la posicion minima supuesta por la posicion del menor del rango y queda en orden
		#cambiazo:
		aux=lista[i] 
		lista[i]=lista[minimo] #el ultimo evaluando pasa a ser el minimo del rango restante
		lista[minimo]=aux #el minimo del rango restante pasa a ser el evaluado
		print(lista) #imprimimos cada cambiazo
#output:
# [5, 4, 3, 2, 1]
# [1, 4, 3, 2, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]

#seleccion()

def prueba():
	#ordenamiento por seleccion
	#usar nombres mnemotecnicos
	#para las variables (3 caracteres)
	lista=[4,2,6,8,5,7,0]
	print(lista)
	for i in range(len(lista)):
		min=i 
		for j in range(i,len(lista)): 
			if lista[j]<lista[min]: 
				min=j 
		aux=lista[i] 
		lista[i]=lista[min] 
		lista[min]=aux 
		print(lista)  

prueba()