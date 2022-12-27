from turtle import*
import turtle

#configuracion del tamaño de la ventana
screen=turtle.Screen()
screen.setup(1100,1100,0,0)#tamaño de la ventana en donde graficaremos
title("Christmas with turtle py") #titulo que queremos que se imprima 
bgcolor('darkblue')#color de fondo
screensize(900,900)#tamalño del area del dibujo

#inicializamos el turtle para el proyecto
t=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()


#dibujamos los segmentos triangulares del arbol
#asignandole coordenadas en el plano
def trazasegmentos(tamanio, cima):
    t.color("forest green") 
    t.speed(1)
    t.pensize(5)
    #t.penup()
    t.begin_fill()
    t.setposition(0,cima)
    t.setposition(tamanio,cima-tamanio)
    t.setposition(-tamanio,cima-tamanio)
    t.setposition(0,cima)
    t.end_fill()
    #t.pendown()

#funcion para pintar un circulo recibimos un objeto turtle , las coordenadas donde queremos dibujar y el radio del circulo
def dibujaCirculo(cursor, x,y,radio,color,velocidad):
    t.penup()
    t.speed(velocidad)
    t.pensize(5)
    t.color(color)
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(radio)
    t.end_fill()

#funcion para pintar estrellas recibimos las coordenadas  y tamaño
def pintaEstrella(x,y, tamanio1,tamanio2):
    #estrella del arbol
    t.penup()
    t.speed(0)
    t.color("gold")
    t.goto(x,y)
    t.begin_fill()
    t.pendown()
    for i in range(5):
        t.forward(tamanio1)
        t.right(tamanio2)
    t.end_fill()   

#funcion que pintara las esferas , recibimos sus coordenadas , la figura de la esfera y el color
def pintaEsfera(x,y , figura , color):
    t.speed(1)
    t.shape(figura)
    t.fillcolor(color)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(90)
    t.stamp()


def pintaTriangulo(x,y,color):
    t.speed(0)
    t.penup()
    t.goto(x,y)
    t.color(color)
    t.begin_fill()
    t.pendown()
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.end_fill()


filename= r"C:\Users\josed\OneDrive\Documentos\ProyectosdeOcio\turtleprojects\cheemsgif.gif"

def pintacuadrado(x,y,color):
    t.speed(0)
    t.penup()
    t.goto(x,y)
    t.color(color)
    t.begin_fill()
    t.pendown()
    t.forward(60)
    t.left(90)

    t.forward(60)
    t.left(90)

    t.forward(60)
    t.left(90)

    t.forward(60)
    t.left(90)
    t.end_fill()


if __name__== "__main__":
    #dibujaremos la luna para esto primero dibujamos el circulo completo
    dibujaCirculo(t,230,180,60,"gold",1)

    #ahora hacemos el dibujo con las medidas de cuarto creciente
    dibujaCirculo(1,200,180,60,"darkblue",1)

    #pintamos algunas estrellas en el cielo 
    pintaEstrella(0,180,40,144)
    pintaEstrella(-20,300,40,144)
    pintaEstrella(-400,200,40,144)
    pintaEstrella(-500,100,40,144)
    pintaEstrella(-200,200,40,144)
    pintaEstrella(200,250,40,144)
    pintaEstrella(300,100,40,144)
    pintaEstrella(400,250,40,144)
    pintaEstrella(-300,250,40,144)
    pintaEstrella(-450,300,40,144)

    t.speed(0)
    #tronco del arbol
    t.penup()
    t.goto(20,-210)
    t.pendown()
    t.color("brown")
    t.pensize(5)
    t.begin_fill()
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(80)
    t.end_fill()


    #dibuja los segmentos del arbol uno por uno
    t.penup()
    trazasegmentos(50, 20)
    trazasegmentos(80, 0)
    trazasegmentos(120, -30)
    trazasegmentos(150, -60)
 

    pintaEstrella(-10,12,40,144)

    #colocamos las esferas en el arbol
    pintaEsfera(10,-109,"circle","red")
    pintaEsfera(-30,-189,"circle","blue")
    pintaEsfera(40,-189,"circle","white")
    pintaEsfera(40,-189,"circle","white")
    pintaEsfera(80,-159,"circle","yellow")
    pintaEsfera(60,-129,"circle","medium spring green")
    pintaEsfera(10,-159,"circle","blue")
    pintaEsfera(-40,-159,"circle","red")
    pintaEsfera(-80,-139,"circle","yellow")
    pintaEsfera(-30,-120,"circle","white")
    pintaEsfera(-80,-189,"circle","medium spring green")
    pintaEsfera(100,-189,"circle","red")
    pintaEsfera(-40,-85,"circle","yellow")
    pintaEsfera(30,-60,"circle","white")
    pintaEsfera(0,-20,"circle","blue")
    pintaEsfera(0,-60,"circle","medium spring green")
    pintaEsfera(-40,-57,"circle","red")
    pintaEsfera(50,-100,"circle","blue")

    pintacuadrado(120,-300,"red")
    
    


    pintacuadrado(-50,-300,"green")
  

    dibujaCirculo(t,-250,-200,80,"white",0)
    dibujaCirculo(t,-260,-100,60,"white",0)
    dibujaCirculo(t,-280,-10,40,"white",0)
    pintaEsfera(-320,-10,"circle" , "orange")
    pintaEsfera(-300,5,"circle" , "black")
    pintaEsfera(-340,5,"circle" , "black")
    pintaEsfera(-320,-100,"circle" , "black")
    pintaEsfera(-320,-130,"circle" , "black")
    pintaEsfera(-320,-160,"circle" , "black")

    pintaTriangulo(-280,10,"red")
    pintaEsfera(-280,110,"circle" , "white")
    
   
    t2.penup()
    t2.goto(300,-200)
    t2.pendown()
    screen.register_shape(filename)
    screen.addshape(filename)
    t2.shape(filename)

    t.penup()
    message="Merry Cheemsmas!!!"
    t.goto(-10,110)
    t.color("spring green")
    t.pendown()
    t.write(message,move=False,align="center",font=("Arial",25,"bold"))
    t.hideturtle()
    


    t3.penup()
    message2="Femliz Namvida!!!"
    t3.goto(-10,60)
    t3.color("red")
    t3.pendown()
    t3.write(message2,move=False,align="center",font=("Arial",25,"bold"))
    t3.penup()
    message3="Y recuerda no tires pirotecnia que me da amsiedad porfis"
    t3.goto(-10,-340)
    t3.color("gold")
    t3.pendown()
    t3.write(message3,move=False,align="center",font=("Arial",25,"bold"))
    t3.penup()
    t3.hideturtle()
    turtle.done()



    
screen.mainloop()