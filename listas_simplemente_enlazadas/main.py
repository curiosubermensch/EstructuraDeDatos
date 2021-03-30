from lista_simple_enlazada import ListaSimpleEnlazada

lista = ListaSimpleEnlazada() #creamos un objeto del tipo (una lista simplemente enlazada)

lista.agregarUltimo(10) #le agregamos un valor al ultimo
lista.agregarUltimo(20)
lista.agregarUltimo(30)
lista.recorreImprime() #10 20 30

#comprobar primero y ultimo
print("primer: ", lista.primero.dato)
print("ultimo: ", lista.ultimo.dato)
print("siguiente del ultimo: ", lista.ultimo.siguiente)
# output:
# primer:  10
# ultimo:  30
# siguiente del ultimo:  None
print("********eliminacion del ultimo*******")
lista.eliminaUltimo()
lista.recorreImprime()

print("*********agregar al inicio***********")
lista.agregarInicio(7)
lista.recorreImprime()

print("*********eliminar al inicio***********")
lista.eliminaInicio()
lista.recorreImprime()