#ordenar de menor a mayor la lista
#l=[5,4,3,2,1]
#print(l)
#5,4,3,2,1 
#4,5,3,2,1 
#4,3,5,2,1 
#4,3,2,5,1 
#4,3,2,1,5 

def burbujaCorto(): #vesion más eficiente
	for i in range(4):
		for j in range(4-i):
			if l[j]>l[j+1]:
				aux=l[j]
				l[j]=l[j+1]
				l[j+1]=aux
			print(l)
""" output:
[5, 4, 3, 2, 1]
[4, 5, 3, 2, 1]
[4, 3, 5, 2, 1]
[4, 3, 2, 5, 1]
[4, 3, 2, 1, 5]
[3, 4, 2, 1, 5]
[3, 2, 4, 1, 5]
[3, 2, 1, 4, 5]
[2, 3, 1, 4, 5]
[2, 1, 3, 4, 5]
[1, 2, 3, 4, 5]
"""
def bubbleSimple():
	for i in range(4):
		for j in range(4):
			if l[j]>l[j+1]:
				aux=l[j]
				l[j]=l[j+1]
				l[j+1]=aux
			print(l)

""" output:
[5, 4, 3, 2, 1]
[4, 5, 3, 2, 1]
[4, 3, 5, 2, 1]
[4, 3, 2, 5, 1]
[4, 3, 2, 1, 5]
[3, 4, 2, 1, 5]
[3, 2, 4, 1, 5]
[3, 2, 1, 4, 5]
[3, 2, 1, 4, 5]
[2, 3, 1, 4, 5]
[2, 1, 3, 4, 5]
[2, 1, 3, 4, 5]
[2, 1, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
"""

def burbujaAlverre():
l=[1,2,3,4]
#ordenar la lista de MAYOR a MENOR, considerar eficiencia
print(l)
for i in range(3): 
	for j in range(3-i): 
		if l[j]<l[j+1]:
			x=l[j] 
			l[j]=l[j+1] 
			l[j+1]=x
		print(l)
""" output:
[1, 2, 3, 4]
[2, 1, 3, 4]
[2, 3, 1, 4]
[2, 3, 4, 1]
[3, 2, 4, 1]
[3, 4, 2, 1]
[4, 3, 2, 1]
"""
burbujaAlverre()