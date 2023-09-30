from turtle import *
import tkinter as tk

size = 50
width(2)
speed(100)

def build_square():
    for i in range(4):
        forward(size)
        left(90)

def build_triangle():
    for i in range(3):
        forward(size)
        left(120)

def build_circle():
    circle(size)

def build_star():
    for i in range(5):
        forward(size)
        right(144)

def build_dogecagon():
    for i in range(12):
        forward(size)
        right(30)

def build_square_circle():
    for i in range(12):
        build_square()
        right(30)

def build_triangle_circle():
    for i in range(12):
        build_triangle()
        right(30)

def build_circle_circle():
    for i in range(12):
        build_circle()
        right(30)

def build_star_circle():
    for i in range(12):
        build_star()
        right(30)

def build_dogecagon_circle():
    for i in range(12):
        build_dogecagon()
        right(30)

def keyboard_input():
    command = input_text.get()

    if command == "квадрат":
        build_square()
    elif command == "треугольник":
        build_triangle()
    elif command == "круг":
        build_circle()
    elif command == "звезда":
        build_star()
    elif command == "догекагон":
        build_dogecagon()
    elif command == "квадрат в круге":
        build_square_circle()
    elif command == "треугольник в круге":
        build_triangle_circle()
    elif command == "круг в круге":
        build_circle_circle()
    elif command == "звезда в круге":
        build_star_circle()
    elif command == "догекагон в круге":
        build_dogecagon_circle()

    elif command == "вправо":
        penup()
        forward(100)
        pendown()
    elif command == "влево":
        penup()
        backward(100)
        pendown()
    elif command == "вверх":
        penup()
        left(90)
        forward(100)
        right(90)
        pendown()
    elif command == "вниз":
        penup()
        right(90)
        forward(100)
        left(90)
        pendown()


commands_label1 = tk.Label(text="круг, квадрат, треугольник, звезда, догекагон", width=100, font=("Arial", 10))
commands_label1.pack()

commands_label2 = tk.Label(text="квадрат в круге, треугольник в круге, круг в круге, звезда в круге, догекагон в круге", width=100, font=("Arial", 10))
commands_label2.pack()

commands_label3 = tk.Label(text="вправо, влево, вверх, вниз", width=100, font=("Arial", 10))
commands_label3.pack()

input_text = tk.Entry(text="Введите название фигуры:", width=100, font=("Arial", 20))
input_text.pack()

button_game = tk.Button(text="Нарисовать", command=keyboard_input, width=100, font=("Arial", 20))
button_game.pack()
done()