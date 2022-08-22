import numpy as np # pip install numpy
from PIL import Image # pip install Pllow
import re 




#GLOBALES

#Busca el primer dato escencial en el archivo txt, el tamaño de la matriz
#busca el unico elemento numerico
def encontrar_tamaño(archivo):
    instrucciones = open(archivo,'r')
    for linea in instrucciones:
        tamaño = re.findall(r'\d+', linea)
        if len(tamaño)!= 0: #Se asegura de retornar el primer valor que contenga un numero en la lista
            tamaño = int(tamaño[0]) #Convierte el unico elemento de la lista a un numero
            return tamaño
    instrucciones.close()

#ENCUENTRA EL PRIMER COLOR QUE ENCUENTRA, EN ESTE CASO, EL COLOR DEL LIENZO
def encontrar_color(archivo):
    instrucciones = open(archivo,'r')
    for linea in instrucciones:
        color= re.findall(r'Rojo|Azul|Blanco|Verde|Negro|RGB.+', linea)
        if len(color)!=0: #Se asegura de retornar el color, la primera linea que contenga la Frase Color de fondo
            color = str(color[0]) #convierte el unico elemento de la lista en un string
            return color #retorna inmediatamente el color del lienzo inicial PARA ASI CREARLO Y QUE NO SIGA BUSCANDO MAS COLORES, ESOS SE IRAN EDITANDO EN OTRAS FUNCIONES
    instrucciones.close()

#RETORNA EL CODIGO CROMATICO RGB DEL LIENZO CON UN COLOR DE FONDO ESPECIFICADO
def Base_de_datos(color):
    colores = {"Rojo":(255,0,0),
               "Verde":(0,255,0),
               "Azul":(0,0,255),
               "Negro":(0,0,0),
               "Blanco":(255,255,255)}
    if color in colores:
        return colores[color] #SI EL COLOR ESTA EN EL DICCIONARIO RETORNA SU CODIGO CROMATICO KEY:VALUE
    else:
        cromaticos = re.findall(r'\d+',color) #SI NO SE ASUME QUE ES UN STRING DEL TIPO "RGB(N,N,N)" POR LO QUE EXTRAE LOS NUMEROS...
        rgb = (int(cromaticos[0]),int(cromaticos[1]),int(cromaticos[2])) #Y LOS GUARDA EN UNA TUPLA
        return rgb
def crear_el_lienzo(n,rgb): #Recibe 2 parametros, el Tamaño y el color ya convertido a tupla
    filas = n #MAS
    columnas = n #ELEGANCIA
    lienzo = []
    for i in range(filas):
        lista = []
        for j in range(columnas):
            lista.append(rgb)
        lienzo.append(lista)#CREA A LA LISTA DE LISTAS NXN CON LOS DATOS DE LAS TUPLAS GENERADAS EN LA FUNCION BASE DE DATOS
    return lienzo


def MatrizAImagen(matriz, filename='pixelart.png', factor=10):
    '''
    Convierte una matriz de valores RGB en una imagen y la guarda como un archivo png.
    Las imagenes son escaladas por un factor ya que con los ejemplos se producirian imagenes muy pequeñas.

        Parametros:
                matriz (lista de lista de tuplas de enteros): Matriz que representa la imagen en rgb.
                filename (str): Nombre del archivo en que se guardara la imagen.
                factor (int): Factor por el cual se escala el tamaño de las imagenes.
    '''
    matriz = np.array(matriz, dtype=np.uint8)
    np.swapaxes(matriz, 0, -1)

    N = np.shape(matriz)[0]

    img = Image.fromarray(matriz, 'RGB')
    img = img.resize((N*10, N*10), Image.Resampling.BOX)
    img.save(filename)
    

#MAIN FUNCION
#EL CODIGO PARTE CREANDO EL LIENZO CON EL CUAL SE EMPEZARA A DIBUJAR (MATRIZ BIDIMENSIONAL RELLENA CON TUPLAS)
n = encontrar_tamaño("instrucciones.txt")
color = encontrar_color("instrucciones.txt")
print(color)
rgb = Base_de_datos(color)
print(rgb)
data = crear_el_lienzo(n,rgb)
print(data)


MatrizAImagen(data)
