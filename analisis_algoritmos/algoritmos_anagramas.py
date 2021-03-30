def anagramaMarcadoVerificacion(cadena1,cadena2):
    unaLista = list(cadena2)

    pos1 = 0
    aunOK = True

    while pos1 < len(cadena1) and aunOK:
        pos2 = 0
        encontrado = False
        while pos2 < len(unaLista) and not encontrado: #ira comparando un elemento de cadena1 con todos los de la lista, si hay coincidencia se seguira verificando
            if cadena1[pos1] == unaLista[pos2]:
                encontrado = True
            else:
                pos2 = pos2 + 1

        if encontrado:
            unaLista[pos2] = None #a medida que se van encontrando coincidencias se van marcando con un "None" en la lista
        else:
            aunOK = False #si no hay ninguna coincidencia se saldra del bucle principal para retornar false

        pos1 = pos1 + 1

    return aunOK

#print(anagramaMarcadoVerificacion('abcd','dcba'))

def anagramaOrdenaCompara(cadena1,cadena2): #O(nlogn)
    unaLista1 = list(cadena1) 
    unaLista2 = list(cadena2) 

    unaLista1.sort() #nlogn #orden albabetico
    unaLista2.sort() #nlogn

    pos = 0
    coincide = True

    while pos < len(cadena1) and coincide: #n
        if unaLista1[pos]==unaLista2[pos]:
            pos = pos + 1
        else:
            coincide = False

    return coincide

#print(anagramaSolucion2('abcde','edcba'))


def anagramaSolucion4(cadena1,cadena2):
    c1 = [0]*26
    c2 = [0]*26
    
    for i in range(len(cadena1)):
        pos = ord(cadena1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(cadena2)):
        pos = ord(cadena2[i])-ord('a')
        c2[pos] = c2[pos] + 1
    print(c1,"\n\n",c2)
    print(len(c1),"\n",len(c2))
    j = 0
    aunOK = True
    while j<26 and aunOK:
        print("j: ",j,"| ¿c1[j]==c2[j]? :",c1[j]," [] ",c2[j])
        if c1[j]==c2[j]:
            j = j + 1
        else:
            aunOK = False

    return aunOK

#print(anagramaSolucion4('abc','cba'))
"""
[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

 [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
26 
 26
j:  0 | ¿c1[j]==c2[j]? : 1  []  1
j:  1 | ¿c1[j]==c2[j]? : 1  []  1
j:  2 | ¿c1[j]==c2[j]? : 1  []  1
j:  3 | ¿c1[j]==c2[j]? : 0  []  0
j:  4 | ¿c1[j]==c2[j]? : 0  []  0
j:  5 | ¿c1[j]==c2[j]? : 0  []  0
j:  6 | ¿c1[j]==c2[j]? : 0  []  0
j:  7 | ¿c1[j]==c2[j]? : 0  []  0
j:  8 | ¿c1[j]==c2[j]? : 0  []  0
j:  9 | ¿c1[j]==c2[j]? : 0  []  0
j:  10 | ¿c1[j]==c2[j]? : 0  []  0
j:  11 | ¿c1[j]==c2[j]? : 0  []  0
j:  12 | ¿c1[j]==c2[j]? : 0  []  0
j:  13 | ¿c1[j]==c2[j]? : 0  []  0
j:  14 | ¿c1[j]==c2[j]? : 0  []  0
j:  15 | ¿c1[j]==c2[j]? : 0  []  0
j:  16 | ¿c1[j]==c2[j]? : 0  []  0
j:  17 | ¿c1[j]==c2[j]? : 0  []  0
j:  18 | ¿c1[j]==c2[j]? : 0  []  0
j:  19 | ¿c1[j]==c2[j]? : 0  []  0
j:  20 | ¿c1[j]==c2[j]? : 0  []  0
j:  21 | ¿c1[j]==c2[j]? : 0  []  0
j:  22 | ¿c1[j]==c2[j]? : 0  []  0
j:  23 | ¿c1[j]==c2[j]? : 0  []  0
j:  24 | ¿c1[j]==c2[j]? : 0  []  0
j:  25 | ¿c1[j]==c2[j]? : 0  []  0
True 
"""