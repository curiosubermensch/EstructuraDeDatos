import math

l=[2,3,5,6,8,11,12,15,17,18,21,23,24,29,30]
buscado=23
#l=[1,2,3,4,5,6,7,8,9,10]
#buscado=8
def busqueda_binaria(l,b):
	medio=(l[0]+l[-1])//2 
	c=0
	while b!=medio:
		if medio>b:
			l=l[0:medio]
		else: 
			l=l[medio+1:]
		medio=(l[0]+l[-1])//2 #el error es que estoy sumando los elementos y no los indices
	return medio

#print(busqueda_binaria(l,buscado))

#l=[1,2,3,4,5,6,7,8,9,10]
#buscado=8
def busquedaBinaria(l,b):
	i=0
	f=len(l)-1
	while i<=f:
		medio=(i+f)//2 #sumamos los INDICES de inicio y fin y los dividimos por 2
		if l[medio]==b:
			return True	
		elif l[medio]<b:
			i=medio+1 #no consideramos el medio xq sabemos que es menor
		elif l[medio]>b: #el elemento podria estar en la porcion más chica
			f=medio-1
	return False
#print(busquedaBinaria(l,buscado))
#output: True

def busquedaBinariaPasos(l,b):
	i=0
	f=len(l)-1
	pasos=0
	while i<=f:
		pasos+=1
		medio=(i+f)//2 
		if l[medio]==b:
			return True, pasos	
		elif l[medio]<b:
			i=medio+1 
		elif l[medio]>b: 
			f=medio-1
	return False, pasos

#datos=[i for i in range(6)] #[0, 1, 2, 3, 4, 5] #ejemplo lista por comprension
a=[i for i in range(1,1000)] 
print(busquedaBinariaPasos(a,999)) #10 pasos
print(math.log(1000,2))

b=[i for i in range(1,10000)]
print(busquedaBinariaPasos(b,9999)) #14
print(math.log(10000,2))

c=[i for i in range(1,100000)]
print(busquedaBinariaPasos(c,99999)) #17
print(math.log(100000,2))

d=[i for i in range(1,1000000)]
print(busquedaBinariaPasos(d,999999)) #19
print(math.log(1000000,2))

e=[i for i in range(1,10_000_000)]
print(busquedaBinariaPasos(e,9_999_999)) #24
print(math.log(10_000_000,2))
"""
(True, 10)
9.965784284662087
(True, 14)
13.28771237954945
(True, 17)
16.609640474436812
(True, 20)
19.931568569324174
(True, 24)
23.25349666421154
"""