#import turtle: Эта строка импортирует модуль turtle целиком. Это означает, что для доступа к функциям, классам и переменным из модуля turtle, вы должны использовать префикс turtle.. Например, turtle.forward(100) вызывает функцию forward из модуля turtle. from turtle import *: Эта строка импортирует все функции, классы и переменные из модуля turtle в текущее пространство имен. Это означает, что вы можете использовать функции и классы напрямую без префикса turtle.. Например, forward(100) вызывает функцию forward из модуля turtle без необходимости указывать префикс.

# mis1
# bread = False
# milk = True
# eggs = False
# result = False
# if not milk or not eggs: #Это условное выражение проверяет два условия. Сначала оно проверяет, является ли milk ложным (с помощью оператора not) или eggs ложным. Если либо milk является ложным, либо eggs является ложным, выполняется внутреннее условное выражение.
#     if not bread:
#         result = True
# print(result)

# mis2
# import turtle
# from turtle import *
# color('blue')
# begin_fill()
# forward(100)
# right(90)
# forward(200)
# right(90)
# forward(100)
# right(90)
# forward(200)
# end_fill()
# done()

# mis4
# from turtle import *
# color('red')
# begin_fill()
# forward(100)
# right(90)
# forward(200)
# end_fill()

# color('blue')
# begin_fill()
# right(90)
# forward(100)
# right(90)
# forward(200)
# end_fill()
# done()

# mis5
# from turtle import *
# color('black')
# begin_fill()
# shape('turtle')
# for i in range(4):
#     forward(100)
#     right(90)
# end_fill()
# done()

# mis6
# from turtle import *
# speed(10)
# color("pink")
# begin_fill()
# circle(100)
# end_fill()
# right(90)

# color("blue")
# begin_fill()
# circle(100)
# end_fill()
# right(90)

# color("black")
# begin_fill()
# circle(100)
# end_fill()
# right(90)

# color("yellow")
# begin_fill()
# circle(100)
# end_fill()
# done()

# # forward(200)
# done()

# my works
# import turtle
# turtle.bgcolor('black')
# squary = turtle.Turtle()
# squary.speed(200)
# squary.pencolor('red')
# for i in range(800):
#     squary.forward(i)
#     squary.left(91)
# turtle.done()

# import turtle
# # Создаем экземпляр черепашки
# t = turtle.Turtle()
# t.speed(0)

# # Задаем цвета пера
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# # Рисуем геометрические фигуры
# for sides in range(3, 10):
#     t.color(colors[sides % 6])  # Переключаем цвет пера
#     for _ in range(sides):
#         t.forward(100)
#         t.left(360 / sides)

# turtle.done()

import turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor('black')

# Задаем цвета пера
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Рисуем психоделический круг
for i in range(200):
    t.pencolor(colors[i % 6])  # Переключаем цвет пера
    t.width(i/100 + 1)
    t.forward(i)
    t.left(59)
    
turtle.done()
