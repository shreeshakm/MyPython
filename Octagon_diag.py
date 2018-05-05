import turtle
import math

length1 = math.sqrt(4 + 2*math.sqrt(2))

def polygon (bob,lenght,n):
    for i in range(0,n):
        bob.fd(lenght)
        bob.lt(360/n)

def diagonal(n,length):
    d_length = length1*length
    diag = int(n/2)
    angle = 360/n
    for i in range(0,diag):
        bob.lt(67.5)
        bob.fd(d_length)
        bob.lt(112.5)
        bob.fd(length)
        bob.lt(45)

bob = turtle.Turtle()
polygon(bob,100,8)
diagonal(8,100)

turtle.mainloop()