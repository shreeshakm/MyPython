import turtle

def polygon (bob,lenght,n):
    for i in range(0,n):
        bob.fd(lenght)
        bob.lt(360/n)

bob = turtle.Turtle()
polygon(bob,100,7)

turtle.mainloop()