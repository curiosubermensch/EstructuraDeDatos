import turtle
import random

#detalles: las luces deberian estar en un rango determinado por una figura geometrica tipo nube
#la estrella deberia posicionarse en base al tamaño del arbol

window=turtle.Screen()
random_colors = ["#0ca90c", "#c20d0d", "#ffffff", "#ffd700", "#3225de", "#8314b9"] #colores navideños
tortuga=turtle.Turtle()
tortuga.speed(0)
window.bgcolor("black")

#direccionar 90 grados hacia la izq 
tortuga.left(90) 

def arbol_recursivo(tamaño,tortuga):
	tortuga.pensize(tamaño/10) #el tamaño de pluma irá disminuyendo por cada llamada
	if tamaño<10:
		#cuando se alcanza el cb llegamos a la punta de la rama, aprovechamos de poner una luz
		tortuga.dot(random.randint(7,10), random.choice(random_colors)) #dot(pixeles, color)
		return
	else:
		tortuga.forward(tamaño) #dibuja tronco
		tortuga.left(45) #ajuste izq
		arbol_recursivo((tamaño-0.2)/1.5,tortuga) #dibuja subrama izq y luego dibuja la sub-subrama izq y derecha
		tortuga.right(90) #ajuste derecha (ramificacion)
		arbol_recursivo((tamaño-0.2)/1.5,tortuga) #dibuja subrama derecha y luego la sub-subrama izq y derecha
		tortuga.left(45) #ajuste direccion retroceso
		tortuga.backward(tamaño) #retroceso

tortuga.penup() #levantamos la pluma para que no dibuje
tortuga.setpos(0,-250) #bajamos en el eje y para tener mas espacio
tortuga.pendown() #bajamos pluma pa seguir escribiendo
tortuga.hideturtle() #ocultar puntero
tortuga.color("brown")


arbol_recursivo(150,tortuga)

tortuga.penup()
tortuga.setpos(-60, 100)
tortuga.pendown()
tortuga.color("yellow")
tortuga.begin_fill() #empezar a rellenar figura
#codigo q dibuja una estrella
for i in range(5):
    tortuga.forward(150)
    tortuga.right(144) #144° a la derecha para hacer una estrella
tortuga.end_fill() #termina rellenado

#LUCES RANDOM:
def luces():
	maxY=200
	maxX=250
	luces=[]
	for j in range(0,10000):
		y=random.randint(-1*maxY,maxY) #coordenada "y" aleatoria [max_negativa, max_positiva]
		x=random.randint(-1*maxX,maxX)
		#las luces tienen q ser una tortuga para poder manipularlas y desaparecerlas con clear()
		luz=turtle.Turtle()
		luz.speed(0)
		luz.hideturtle() #esconderla
		luz.penup()
		luz.setpos(x,y) #setear en la posicion aleatoria generada
		luz.pendown()
		luz.dot(random.randint(1,5), random.choice(random_colors)) #dibujo de la luz (pixeles random,color random)
		luces.append(luz) #agregar la luz a la lista
		#efecto titilante 
		if len(luces)>100: #si hay mas de 100 luces en el lienzo
		    luzApagar=random.choice(luces)
		    luzApagar.clear()

luces()

window.exitonclick()