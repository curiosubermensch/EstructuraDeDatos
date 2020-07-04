#BORRADOR PYTHON


# n = int(input())
# for i in range(n):
#     a, b = input().strip().split(' ')
#     print (int(a) + int(b))

#!/bin/python3

import math
import os
import random
import re
import sys

#los evaluados deben ser descartados
#

n=12
ar=[]
for j in range(n):
    x=random.randint(1,10)
    ar.append(x)
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    if 1<=n and n<=100:
        sinRepetir=list(set(ar)) #removemos los duplicados
        totalPares=0
        for i in sinRepetir: #recorrerá solo los elementos una vez 
            totalPares+=ar.count(i) // 2 #al dividir por dos (sin resto) la cant de calcetines obtenemos la cantidad de pares
            # // --> division por integer
        return totalPares

    else:
        return "error"


#print(ar)
#print(sockMerchant(n,ar))

# Complete la función countingValleys en el editor a continuación. Debe devolver un número entero que denote el número de valles que atravesó Gary.

# countingValleys tiene los siguientes parámetros:

# n : el número de pasos que da Gary
# s : una cadena que describe su camino

def countingValleys(n,s):
    pass

#c[i+1]==c[len(c)-1] na que ver pos compara los 0 por eso da error, se tienen que comparar los indices #nomas no los elementos porque esos coincidiran muy prob

def jumpingOnClouds(c):
    saltos=0
    i=0
    while i<len(c)-1:
        print("-------------vuelta nro",i+1,"-------------")
        print("valor de i:",i)
        if c[i]==0 and i+1==len(c)-1: 
            saltos+=1
            print("primer if i:",i)
        else:
            if c[i] == 0 and (c[i+1]==0 or c[i+1]==1) and c[i+2]==0:
                saltos+=1
                i+=1
                print("segundo if i:",i)
            elif c[i]==0 and c[i+1]==0 and c[i+2]==1:
                saltos+=1
                print("elif i:",i)
        i+=1
    return saltos 

#print(jumpingOnClouds([0,0,0,1,0,0]))

def jumpingOnClouds(c):
    saltos=0
    i=0
    while i<len(c)-1:
        if c[i]==0 and i+1==len(c)-1: 
            saltos+=1
        else:
            if c[i] == 0 and (c[i+1]==0 or c[i+1]==1) and c[i+2]==0:
                saltos+=1
                i+=1
                
            elif c[i]==0 and c[i+1]==0 and c[i+2]==1:
                saltos+=1
        i+=1
    return saltos 


def generadorS(s,n):
    s=s*n
    yield s 

def repeatedString(s, n):
    print("string a repetir: ",s)
    print("lenSubstring: ",n)
    print(s)
    cadenazo=generadorS(s,n)


    return cadenazo.count("a",0,n)


print(repeatedString("a",20))