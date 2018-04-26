import turtle

square = turtle.Turtle()
print(square)

for i in range(0,4):
    square.fd(100)
    square.lt(90)

turtle.mainloop()