import random

def crear_censo(n):
	censo=[]
	alfabeto="ABCDEFGHIJKLMNÑOPQRSTUAEIOU"
	numero=0 #id propio de cada persona

	print("creando censo...")

	for i in range(n):
		aumento=random.randint(1,2)
		numero+=aumento #aumenta en 1 o 2
		letras=random.sample(alfabeto,5) #sample retornará 5 elementos del string alfabeto
		nombre="".join(letras) #la lista letras la transformará en un string concatenado
		edad=random.randint(18,99)
		impuestos=random.choice((True,True,True,False))
		censo.append([numero,nombre,edad,impuestos])

		if len(censo) % 10==0:
			print("creados",len(censo),"registros")

	print("censo creado")
	print("ultimo registro: ",censo[-1])
	return censo


#1. buscar por numero
#2. buscar por nombre
#3. salir

def buscaxnombre(lista,nom):  #tiene que ser lineal nomas la busqueda
	encontrados=[]
	for i in range(len(lista)):
		if lista[i][1]==nom:
			encontrados.append(lista[i])
	if len(encontrados)>0:
		return encontrados
	else:
		return None


def buscaxnumero(lista,n): #busqueda binaria para mayor eficiencia
	i=0
	f=len(lista)-1
	while i<=f:
		m=(i+f)//2
		if lista[m][0]==n:
			return lista[m]
		elif lista[m][0]>n: #nos sirve el pedazo de la izq
			f=m-1
		elif lista[m][0]<n: #nos sirve el pedazo de la derecha
			i=m+1
	return "no se encuentra"


def main():
	lista=crear_censo(10_000)
	while True:
		print("1. buscar por numero \n2. buscar por nombre \n3. salir")
		r=int(input())
		if r==1:
			n=int(input("ingrese numero: "))
			print(buscaxnumero(lista,n))
		elif r==2:
			nom=input("ingrese nombre: ")
			print(buscaxnombre(lista,nom))
		elif r==3:
			break
		#1. buscar por numero
#2. buscar por nombre
#3. salir
main()