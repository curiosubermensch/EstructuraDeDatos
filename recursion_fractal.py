import turtle

window=turtle.Screen()

tortuga=turtle.Turtle()
tortuga.speed(0)

#direccionar 90 grados hacia la izq 
tortuga.left(90) 

def fractal():
	#DIBUJAR RAMA PRINCIPAL:
	tortuga.forward(100) #mover 100 pixeles en la direccion q está

	#DIBUJAR SUB-RAMA IZQ
	tortuga.left(45) #direccionar 45 grados a la izq 
	tortuga.forward(50) #mover 50 pixeles a la derecha

	#DIBUJAR SUB-SUB-RAMA IZQ
	tortuga.left(45) #direccionar 45 grados a la izq 
	tortuga.forward(25) #mover 25 pixeles a la derecha
	tortuga.backward(25) #retroceder lo avanzado

	#DIBUJAR SUB-SUB-RAMA DERE
	tortuga.right(90) #direccionar a la derecha
	tortuga.forward(25)
	tortuga.backward(25) #retrocedemos a la sub-rama 

	#RETROCEDER A LA RAMA PRINCIPAL
	tortuga.left(45)
	tortuga.backward(50)

	#DIBUJAR SUB-RAMA DERECHA
	tortuga.right(90)
	tortuga.forward(50)

	#DIBUJAR SUB-SUB-RAMA IZQ
	tortuga.left(45)
	tortuga.forward(25)
	tortuga.backward(25)

	#DIBUJAR SUB-SUB-RAMA DERECHA
	tortuga.right(90)
	tortuga.forward(25)
	tortuga.backward(25) #retroceder a la sub-rama

	#RETROCEDER A LA RAMA PRINCIPAL
	tortuga.left(45)
	tortuga.backward(50) 

	


def arbol_recursivo(tamaño,tortuga):
	if tamaño<10:
		return
	else:
		tortuga.forward(tamaño) #dibuja tronco
		tortuga.left(45) #ajuste izq
		arbol_recursivo(tamaño/2,tortuga) #dibuja subrama izq y luego dibuja la sub-subrama izq y derecha
		tortuga.right(90) #ajuste derecha (ramificacion) debe ser el doble q a la izq para que se ajuste
		arbol_recursivo(tamaño/2,tortuga) #dibuja subrama derecha y luego la sub-subrama izq y derecha
		tortuga.left(45) #ajuste direccion retroceso
		tortuga.backward(tamaño) #retroceso


arbol_recursivo(50,tortuga)