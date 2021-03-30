import turtle

def triangulo(p,t):
	t.up() #Levante el bolígrafo, no dibuje al moverlo.
	t.goto(p[0]) #goto(0,100) 
	t.down()
	t.goto(p[1]) #goto(100,-50)
	t.goto(p[2]) #goto(-100,0)	
	t.goto(p[0])

def mitad(p1,p2): #recibe dos array c/u con dos valores, en otras palabras recibe dos coordenadas [x,y]
	return (p1[0]+p2[0])/2, (p1[1]+p2[1])/2

def sierpinski(p,grado,t):
	#dibujarTriangulo(puntos,miTortuga) #dibujara un triangulo en base a el multiarray de 3 coordenadas
	triangulo(p,t)
	if grado > 0:
		m1=mitad(p[0],p[1])
		m2=mitad(p[1],p[2])
		m3=mitad(p[2],p[0])
		sierpinski([p[0],m1,m3],grado-1,t)
		sierpinski([p[1],m1,m2],grado-1,t)
		sierpinski([p[2],m2,m3],grado-1,t)

def main():
    t = turtle.Turtle()
    miVentana = turtle.Screen()
    t.speed(0)
    puntos = [[0,0],[100,100],[200,0]]
    sierpinski(puntos,5,t)
    miVentana.exitonclick()

main()