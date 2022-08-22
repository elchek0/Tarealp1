import numpy as np
import re
#GLOBALES

#Colores Disponibles
colores = {"Rojo":(255,0,0),
           "Verde":(0,255,0),
           "Azul":(0,0,255),
           "Negro":(0,0,0),
           "Blanco":(255,255,255)}



# Encuentra el Tamaño de la matriz y lo devuelve como una lista de un solo numero
def encontrar_tamaño(archivo):
    instrucciones = open(archivo,'r')
    for linea in instrucciones:
        tamaño = re.findall(r'\d+', linea)
        if len(tamaño)!= 0: #Se asegura de retornar el primer valor que contenga un numero en la lista
            tamaño = int(tamaño[0]) #Convierte el unico elemento de la lista a un numero
            return tamaño
    instrucciones.close()

def encontrar_color(archivo):
    instrucciones = open(archivo,'r')
    for linea in instrucciones:
        color= re.findall(r'Rojo|Verde|Azul|Blanco|Negro|RGB.+', linea)
        if len(color)!=0: #Se asegura de retornar el color, la primera linea que contenga la Frase Color de fondo
            color = str(color[0]) #convierte el unico elemento de la lista en un string
            return color #retorna inmediatamente el color del lienzo inicial
    instrucciones.close()

def Base_de_datos(color):
    colores = {"Rojo":(255,0,0),
            "Verde":(0,255,0),
           "Azul":(0,0,255),
           "Negro":(0,0,0),
           "Blanco":(255,255,255)}
    if color in colores:
        return colores[color]
    else:
        cromaticos = re.findall(r'\d+',color)
        rgb = (int(cromaticos[0]),int(cromaticos[1]),int(cromaticos[2]))
        return rgb


def crear_el_lienzo(n):
    color = encontrar_color("instrucciones.txt")
    filas = n
    columnas = n
    lienzo = []
    for i in range(filas):
        lista = []
        for j in range(columnas):
            lista.append((255,0,0))
        lienzo.append(lista)
    return lienzo
    



