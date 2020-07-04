#crear funcion potencia de manera recursiva:
#ej:  2^4=16

#2^4 = (2^3)*2 = (2^2)*2*2 = (2^1)*2*2*2 = (2^0)*2*2*2*2 = 1*2*2*2*2
#con el 1 calculamos todos los demas

def fpotencia(b,e):
	if e==0:
		return 1
	else:
		return b*fpotencia(b,e-1)

print(fpotencia(2,4)) 
#output: 16


