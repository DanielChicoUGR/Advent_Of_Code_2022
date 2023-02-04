import numpy as np 


def read_data(dir):

    l=[]
    with open(dir,'r') as ifile:
        lineas=ifile.read().splitlines()
    for linea in lineas:
        
        
        l.append( linea )

    return l

PRIOBASEMIN = ord("a")-1    # 96
PRIOBASEMAY = ord("A")-1    # 64

def prioridad(letra:chr)-> int:
    if letra.islower():
        return ord(letra)-PRIOBASEMIN
    else:
        return ord(letra)-PRIOBASEMAY+26


    return 0

datos =read_data('D3/input.txt')

# print(datos)

def Ej1():
    prio=0
    for linea in datos:
        d1=linea[:int(len(linea)/2)]
        d2=linea[int(len(linea)/2):]
        letras_comunes=''.join(set(d1).intersection(d2))
        # for letra in letras_comunes:
            # prio+=prioridad(letra)\
        
        prio+=prioridad(letras_comunes)

    print(prio)

def Ej2():
    prio=0

    for i in range(0,len(datos),3):
        


Ej1()