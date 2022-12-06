#!/bin/python3

from enum import Enum

class Jugada(Enum):
    Rock=1
    Paper=2
    Scissors=3

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f'{cls_name}'

class Estado(Enum):
    win=1
    loose=2
    draw=3

    def __repr__(self):
        cls_name = self.__class__.__name__
        return f'{cls_name}'


archivo_input="input.txt"

def lee_datos(archivo: str )-> list:
    l=[]
    with open(archivo,'r') as ifile:
        for linea in ifile:
            l.append([linea[0],linea[2]])
    # print(f'{l}')
    return l


def puntos_jugada(elfo:Jugada,tu:Jugada)->int:
    a:int=0
    if tu==Jugada.Rock:
        if elfo==Jugada.Rock:
            a= 3
        elif elfo==Jugada.Paper:
            a= 0
        elif elfo==Jugada.Scissors:
            a= 6

    elif tu==Jugada.Paper:
        if elfo==Jugada.Rock:
            a= 6
        elif elfo==Jugada.Paper:
            a= 3
        elif elfo==Jugada.Scissors:
            a= 0

    elif tu==Jugada.Scissors:
        if elfo==Jugada.Rock:
            a= 0
        elif elfo==Jugada.Paper:
            a= 6
        elif elfo==Jugada.Scissors:
            a= 3
    
    return a

def mi_jugada(j:Jugada)-> int:

    if j==Jugada.Rock:
        return 1
    elif j==Jugada.Paper:
        return 2
    elif j==Jugada.Scissors:
        return 3
    
    return 0

def get_jugada(letra:chr)->Jugada:
    letra=letra.capitalize()
    if letra=='A' or letra=='X':
        return Jugada.Rock
    elif letra=='B' or letra=='Y':
        return Jugada.Paper
    elif letra=='C' or letra=='Z':
        return Jugada.Scissors

def get_movement(game)-> Jugada:

    if game in [['A', 'X'], ['B', 'Z'], ['C', 'Y']]:
        return Jugada.Scissors
    elif game in [['A', 'Y'], ['B', 'X'], ['C', 'Z']]:
        return Jugada.Rock
    elif game in [['A', 'Z'], ['B', 'Y'], ['C', 'X']]:
        return Jugada.Paper



def Ej1(datos):
    ptos_totales=0
    for game in datos:
        jelfo=get_jugada(game[0])
        jyo=get_jugada(game[1])
        ptos_totales+=(mi_jugada(jyo)+puntos_jugada(jelfo, jyo))
    print (f'{ptos_totales}')


def Ej2(datos):
    ptos_totales=0
    for game in datos:
        jelfo=get_jugada(game[0])
        jyo=get_movement(game)
        ptos_totales+=(mi_jugada(jyo)+puntos_jugada(jelfo, jyo))
    print(f"{ptos_totales}")


def main():
    datos=lee_datos(archivo_input)

    Ej1(datos)

    Ej2(datos)


if __name__=="__main__":
    main()
# print(a)