import  turtle
import colours as colours
#t = turtle.Turtle()
turtle.bgcolor('black')
turtle.color('blue')
turtle.speed(0)

for i in range(5):
   for colours in ['red','magenta','blue','cyan','green','yellow','white']:
       turtle.color(colours)
       turtle.pensize(3)
       turtle.left(12)
       turtle.forward(200)
       turtle.left(90)
       turtle.forward(200)
       turtle.left(90)
       turtle.forward(200)
       turtle.left(90)
       turtle.forward(200)
       turtle.left(90)






