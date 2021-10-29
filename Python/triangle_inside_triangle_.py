# -*- coding: utf-8 -*-
"""Triangle inside triangle .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T00ptMhOU0EmUsTxP048gULKChP3k87D

# Drawing triangle inside triangle with the help of turtle module
"""

# import the turtle modules
import turtle


# define the function
# for triangle
def form_tri(side):
	for i in range(3):
		my_pen.fd(side)
		my_pen.left(120)
		side -= 10

		
# Forming the window screen
tut = turtle.Screen()
tut.bgcolor("green")
tut.title("Turtle")

my_pen = turtle.Turtle()
my_pen.color("orange")

tut = turtle.Screen()		

# for different shapes
side = 300
for i in range(10):
	form_tri(side)
	side -= 30