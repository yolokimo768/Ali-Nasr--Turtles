# basic turtles
import turtle

# loads turles code/module
t = turtle.Turtle() #creates Turtle

u= 20
num = input ('how many times do u want a triangle drawn in a loop: ')
# Adds a color to the drawing 
color = input('what color would u like the drawings to be: ')
y = 0 

while y < int(num) :
     y= y+1
     print(y)
     t.pencolor(color)
     t.right(45)
     t.forward(u*5)
     t.left (135)
     t.forward(u*5)
     t.left (112)
     t.forward (u*4)
     t.left (20)


input ('hit . to exit')
     
     
