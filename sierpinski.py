import turtle
import time

#goto()
# x - un número o un par/vector de números
# y - un número o ninguno (None)
# Si y es None, x debe ser un par de coordenadas o un Vec2D (por ejemplo, como lo devuelve pos ()).
# Mueva la tortuga a una posición absoluta


def dibujarTriangulo(puntos,t):
    t.up() #Levante el bolígrafo, no dibuje al moverlo.
    t.goto(puntos[0][0],puntos[0][1]) #goto(-100,-50) 
    t.down()
    t.goto(puntos[1][0],puntos[1][1]) #goto(0,100) 
    t.goto(puntos[2][0],puntos[2][1]) #goto(100,-50)
    t.goto(puntos[0][0],puntos[0][1]) #goto(-100,0)

def triangulo(puntos,color,t):
    t.fillcolor(color)
    t.up() 
    t.goto(puntos[0]) #goto(0,100) 
    t.down()
    t.begin_fill()
    t.goto(puntos[1]) #goto(100,-50)
    time.sleep(4)
    t.goto(puntos[2]) #goto(-100,0)	
    time.sleep(4)
    t.goto(puntos[0])
    t.end_fill()


def mitad(p1,p2): #recibe dos array c/u con dos valores, en otras palabras recibe dos coordenadas [x,y]
	return (p1[0]+p2[0])/2, (p1[1]+p2[1])/2 #promedio de x y promedio de y


#hacer seguimiento en grado 2
def sierpinski(p,grado,miTortuga):
	#dibujarTriangulo(puntos,miTortuga) #dibujara un triangulo en base a el multiarray de 3 coordenadas
	colores = ['yellow','orange','red']
	triangulo(p,colores[grado],miTortuga)
	time.sleep(3)
	if grado > 0:
		#1ra llamada: 
	    sierpinski([p[0], #[-100,-50]
	                    mitad(p[0], p[1]), #mitad([-100,-50],[0,100])
	                    mitad(p[0], p[2])], #mitad([-100,-50],[100,-50])
	               grado-1, miTortuga)
	    time.sleep(3)
	    sierpinski([p[1],
	                    mitad(p[0], p[1]), #mitad([],[])
	                    mitad(p[1], p[2])], #mitad([],[])
	               grado-1, miTortuga)
	    time.sleep(3)
	    sierpinski([p[2],
	                    mitad(p[2], p[1]), #mitad([],[])
	                    mitad(p[0], p[2])], #mitad([],[])
	               grado-1, miTortuga)
def main():
   t = turtle.Turtle()
   miVentana = turtle.Screen()
   t.speed(1)
   puntos = [[-100,-50],[0,100],[100,-50]]
   #puntos = [[-300,-150],[0,300],[300,-150]]
   sierpinski(puntos,2,t)
   #triangulador(puntos,t)
   miVentana.exitonclick()


main()