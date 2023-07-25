import turtle

turtle.speed(100)
def sq(a):#можно а убрать и ничего не передавать в аргумент
	for i in range(4):
		turtle.forward(a)
		turtle.left(90)
# sq(100)
# sq(50)

lenght = 30
# turtle.color('purple')
colors = ['blue', 'red', 'black', 'purple']
for i in range(50):
	turtle.color(colors[i%4])
	sq(lenght)
	# turtle.circle(lenght)
	turtle.right(10)
	lenght+=4

# turtle.forward(100)
# turtle.right(10)
# turtle.forward(100)


# turtle.done()