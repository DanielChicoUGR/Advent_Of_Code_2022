

# Archivo_datos='D1/input.txt'
Archivo_datos='input.txt'

elfos={}

def Ej1():
    n_elfos=0
    mas_gordo=0
    max_kal=0
    kal_actuales=0
    with open(Archivo_datos,'r') as ifile:
        
        for linea in ifile:
            
            if linea=='\n':
                if kal_actuales>max_kal:
                    mas_gordo=n_elfos
                    max_kal=kal_actuales
                elfos[n_elfos]=kal_actuales
                n_elfos+=1
                kal_actuales=0
            else:
                kal_actuales+=int(linea)
    
    print (f"El elfo mas gordo es el numero {mas_gordo} y lleva para el viaje {max_kal} Kalorias")
    # print(elfos)

    
def Ej2():
    import operator

    elfo_glotones=sorted(
        elfos.items(),
        key=operator.itemgetter(1),
        reverse=True)

    totalK=0
    otro= enumerate(elfo_glotones)
    
    n=0
    for elfo in otro:
        # print(f"Elfo n°->{elfo[1][0]} lleva encima->{elfos[elfo[1][0]]}")
        totalK+=elfos[elfo[1][0]]
        n+=1
        if(n==3):
            break
        # totalK+=elfos[elfo[1][0]]
    

    
        

    print (totalK)


Ej1()

Ej2()

