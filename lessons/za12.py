# mis1
# from turtle import *
# bgcolor('lightblue')
# color('yellow')
# begin_fill()
# for i in range(4):
#     forward(150)
#     right(90)
# end_fill()

# right(90)
# color('blue')
# begin_fill()
# for i in range(4):
#     forward(150)
#     right(90)
# end_fill()

# left(90)
# color('green')
# begin_fill()
# for i in range(4):
#     forward(150)
#     left(90)
# end_fill()

# left(90)
# color('red')
# begin_fill()
# for i in range(4):
#     forward(150)
#     left(90)
# end_fill()
# done()

# mis2
# for i in range(70, 100):
#     print(i)

# mis3
# for i in range(300, 501):
#     print(i)

# mis4
# for i in range(700, 1001, 100):
#     print(i)

# mis6
# from turtle import *
# bgcolor('lightblue')
# color('pink')
# begin_fill()
# for i in range(8):
#     forward(100)
#     right(45)
# end_fill()
# done()

# from turtle import *
# bgcolor('lightblue')
# width(5)
# color('pink')
# begin_fill()

# forward(100)
# right(45)
# forward(100)
# right(45)
# forward(100)
# right(45)
# forward(100)
# right(45)
# forward(100)
# right(45)
# forward(100)
# right(45)
# forward(100)
# right(45)
# forward(100)
# right(45)

# end_fill()
# done()



# # mis8-13. this code work together IMPORTANT!!!
# from turtle import *
# bgcolor('lightblue')
# color('grey')
# begin_fill()
# for i in range(4):
#     if i % 2 == 0:
#         forward(150) #width malenkoy podstavki
#     else:
#         forward(20) #hight m. podstavki
#     right(90)
# end_fill()

# # mis9
# penup()
# forward(60)
# pendown()

# color('white')
# begin_fill()
# for i in range(4):
#     if i%2==0:
#         forward(30)#width 2d podstavki
#     else:
#         forward(40)#height 2d podstavki
#     left(90)
# end_fill()

# # mis10
# penup()
# left(90)
# forward(40)
# left(90)
# forward(130)
# pendown()

# color('grey')
# begin_fill()
# for i in range(4):
#     right(90)
#     if i%2==0:
#         forward(200)#height monitor
#     else:
#         forward(300)#width monitor
# end_fill()

# # mis11
# penup()
# right(90)
# forward(20)
# right(90)
# forward(20)
# pendown()

# color('black')
# begin_fill()
# for i in range(4):
#     if i%2==0:
#         forward(260)#width black monitor
#     else:
#         forward(160)#height black m
#     left(90)
# end_fill()

# # mis12
# penup()
# forward(115)
# right(90)
# forward(10)
# pendown()

# color("white")
# begin_fill()
# circle(7.5)
# end_fill()

# # mis13
# penup()
# left(180)
# forward(10)
# left(90)
# forward(115)
# pendown()

# color('green')
# begin_fill()
# right(90)
# for i in range(4):
#     if i%2==0:
#         forward(40)
#     else:
#         forward(260)
#     right(90)
# end_fill()
# # moon
# penup()
# forward(160)
# right(90)
# forward(210)
# right(90)
# forward(30)
# pendown()

# color('white')
# begin_fill()
# circle(15)
# end_fill()

# penup()
# left(90)
# forward(15)
# pendown()
# done()

# from turtle import *
# bgcolor('black')
# color('dark orange')
# speed(200)
# f = 1
# for i in range(500):
#     forward(f)
#     left((360/6) + 1)
#     f += 1
# done()

# for i in range(6):
#     forward(100)
#     right(360/6)
# done()

# from turtle import *
# bgcolor("black")
# speed(10000)
# f = 1
# color("white")
# for i in range(1000):
#     forward(f)
#     right(46)
#     f += 1
# done()

from turtle import *
bgcolor("black")
speed(200)


f = 1
color("white")
for i in range(300):
    forward(f)
    right(46)
    f += 1
color("orange")
# right(180)
for i in range(300):
    forward(f)
    right(46)
    f -= 1
color("red")
right(180)
for i in range(300):
    forward(f)
    right(46)
    f += 1
done()