lista=[14,26,39,7,4,8,6,4,2,33,55,23]
#el peor de los casos es 23
dato=23

def busqueda_linea(lista,buscar):
	for elemento in lista: #n operaciones
		if elemento==buscar: #1 op
			return True #1 op
	return False #1 op

#nro operaciones: n (el bucle, lo demas no importa mucho)

if busqueda_linea(lista,dato):
	print("dato encontrado")
else:
	print("dato no encontrado")