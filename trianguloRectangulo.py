#importar las paqueterias 
import matplotlib.pyplot as plt
import numpy as np
#Declarar las variables x & y
x = 14
y = 14
#Colocamos el título del gráfico
plt.title("Representacion del Triangulo Rectangulo")
def generadorDeCoordenadasTriangle(x,y): 
    coo1 = [0,2,4,6,8]
    coo2 = [0,2,4,6,8]
    #Crear el ciclo for y la variable i
    for i in range(1):
        if x==y:
            coo1.insert(0,x)
            coo2.insert(0,y)
                       
            coo1.insert(1,x+1)
            coo2.insert(1,y)
                       
            coo1.insert(2,x+1)
            coo2.insert(2,y+1)
            
            coo1.insert(3,x)
            coo2.insert(3,y+1)
                       
            coo1.insert(4,x)
            coo2.insert(4,y)
                        
    x = np.array([coo1])
    y = np.array([coo2])
    return x, y 
#Generador de CoordenadasTriangle(x & y)
cooS = generadorDeCoordenadasTriangle(x,y)
x = cooS[0]
y = cooS[1]

xelem1 = x[0,0]
xelem2 = x[0,1]
xelem3 = x[0,2]
xelem4 = x[0,3]
xelem5 = x[0,4]

yelem1 = y[0,0]
yelem2 = y[0,1]
yelem3 = y[0,2]
yelem4 = y[0,3]
yelem5 = y[0,4]

x = np.array([xelem1,xelem2,xelem3,xelem4,xelem5])
y = np.array([yelem1,yelem2,yelem3,yelem4,yelem5])

def aristasUno(x,y): # es la line 1
    for i in x: 
        x = x + 1
        plt.plot(x, y)
        
    for i in y: # es la altura
        y = y + 1
        plt.plot(x, y)
    
aristasUno(x,y)  # es la base
for i in range(4): 
    x = x + 1
    y = y + 1 
    plt.plot(x,y)
    #ejecutar llamando a la libreria para que nos muetsre el grafico     
    #Colocamos las etiquetas de los ejes
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")

plt.show()