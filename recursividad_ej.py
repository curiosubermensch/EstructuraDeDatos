def a(b,e):
    if e==0:
        print("fin")
    else:
        print(b*a(b,e-1))

#sumar una lista de manera recursiva:
l=[1,2,3,4,5]

def suma(l,i):
    if i+1==len(l):
        print("sumatoria: ",end=" ")
        return l[i+1]
    else:
        l[i+1]=l[i]+l[i+1]
        print(l[i+1])
        return suma(l,i+1)
        
        

lili=[5,10,15,20,25]
def suma(l,i):
    if i==-len(l):
        print("sumatoria: ",end=" ")
        print(l[-len(l)])
    else:
        l[i-1]=l[i-1]+l[i]
        print(l[i-1])
        return suma(l,i-1)

#suma(lili,-3)
    
#imprimir numeros de 1 al 5 recursivo:

def printer(a,b):
    if a==b:
        print(a)
    else:
        print(a)
        return printer(a+1,b)


