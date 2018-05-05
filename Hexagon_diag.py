import turtle

def polygon (bob,lenght,n):
    for i in range(0,n):
        bob.fd(lenght)
        bob.lt(360/n)

def diagonal(n,length):
    d_length = 2*length
    diag = int(n/2)
    angle = 360/n
    for i in range(0,diag):
        bob.lt(360/n)
        bob.fd(d_length)
        bob.lt(angle*2)
        bob.fd(length)
        bob.lt(angle)

bob = turtle.Turtle()
polygon(bob,100,6)
diagonal(6,100)

turtle.mainloop()