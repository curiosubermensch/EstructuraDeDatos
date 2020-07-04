#dados dos numeros enteros a>=0 y b>0, calcular el resto de su division entera a/b
#print(3.5//2) #1.0 

#1. caso base --->a<b
#2. tipo e hipotesis
#3. caso general para un caso mas que el primero

##################################################################################


def resto(a,b):
	if a<b:
		return 0 #¿o a?
	else:
		return 1 + resto(a-b,b)

print("17//5 = ",17//5)
print("17%5 = ",17%5)
print("15%5 =",15%5)
print("5%7 = ",5%7)

#print(resto(127,5))