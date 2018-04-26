import turtle

square = turtle.Turtle()
print(square)

for i in range(0,360):
    square.fd(1)
    square.lt(1)

turtle.mainloop()