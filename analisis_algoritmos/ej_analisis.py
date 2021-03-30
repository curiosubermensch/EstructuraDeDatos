# Extraer el número de coches y el número de motos que pasan por una autopista, a partir del número de vehículos que cuenta una cámara, y el número de ruedas que cuentan unas gomas en el suelo. Hacerlo con el algoritmo más eficiente.

#vehiculos=6 #4 autos, 2 motos --->4*4+2*2=16+4=20
#ruedas=20
def f(v,r):
	a=(r-2*v)/2
	m=v-a
	if int(m)+int(a)==v:
		print("autos: ",int(a),"; motos:",int(m))
	else:
		print("error")
f(6,20)
