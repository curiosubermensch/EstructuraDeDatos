import turtle
#dibujar triangulo

window=turtle.Screen()
t=turtle.Turtle()
t.hideturtle()
t.speed(1)
t.penup()
t.setpos(-300,-200)
t.pendown()

t.st()
t.forward(200) #dibujo base
t.left(120) #ajuste para dibujar lado
t.forward(200) #dibujo lado
t.left(120)
t.forward(200)
t.right(180)



def sierpinski(l): #meterle 50 que es la mitad
	if l<10:
		return
	else:
		t.forward(l/2)
		t.right(60)
		t.forward(l/2)
		t.right(120)
		t.forward(l/2)
		t.right(120)
		t.forward(l/2)
		t.right(60)
		sierpinski(l/2)
sierpinski(200)

window.exitonclick()
