# mis1
# for i in range(50, 151):
#     if i % 10 == 0:
#         print(i)
#     else:
#         i+=1


# mis2
# def myFirstFunction(a,b):
#     return a-b

# def calculate(num1, num2):
#     krujka = (num1 * num2) + 2
#     return krujka

# nasheReshenie = calculate(7, 9)
# print(nasheReshenie)

# print(calculate(7, 9))
# print(7 * 9 + 2)
# print('Function:', calculate(10, 76, 10)) #1
# print('Function:', calculate(5, 72, 76))


# vichislenie1 = 10
# vichislenie2 = 76
# time1 = 10
# result = (vichislenie1 * vichislenie2 * time1) / 100
# print('dont function:', result)

# vichislenie3 = 5
# vichislenie4 = 72
# time2 = 76
# result2 = (vichislenie3 * vichislenie4 * time2) / 100
# print('dont function:', result2)

# mis3
def sum_every_third_number(start, end):
    total = 0
    for i in range(start, end + 1):
        if i % 3 == 0:
            total += i
    return total

print(sum_every_third_number(1, 9))

# mis5
# from turtle import *
# bgcolor('black')
# width(5)

# def draw_square(c, size):
#     for i in range(4):
#         color(c)
#         forward(size)
#         left(90)

# draw_square('red', 100)
# draw_square('blue', 120)
# draw_square('green', 140)
# draw_square('purple', 160)
# done()

# from turtle import *
# bgcolor('black')
# width(5)
# def draw_triugolnik(c, size, ugol):
#     for i in range(ugol):
#         color(c)
#         forward(size)
#         left(360/ugol)
# draw_triugolnik('red',100,3)
# draw_triugolnik('blue',120,3)
# draw_triugolnik('green',140,3)
# draw_triugolnik('yellow',160,3)
# draw_triugolnik('orange',180,3)
# draw_triugolnik('purple',200,3)
# done()

# mis6
# from turtle import *
# bgcolor('black')
# width(5)
# def draw_something(c, size, ugol):
#     for i in range(ugol):
#         color(c)
#         forward(size)
#         left(360/ugol)
# draw_something('red',100,6)
# draw_something('blue',120,6)
# draw_something('green',140,6)
# draw_something('yellow',160,6)
# draw_something('orange',180,6)
# draw_something('purple',200,6)
# done()