import turtle
import math

x = math.sqrt(2)
t = turtle.Turtle()

def rt120_fd():
    t.rt(120)
    t.fd(100)

def lt120_fd():
    t.lt(120)
    t.fd(100)

def rt90_fd():
    t.rt(90)
    t.fd(100)

def lt90_fd():
    t.lt(90)
    t.fd(100)

def lt75_fd_diag():
    t.lt(75)
    t.fd(100*x)

def lt120_fd_diag():
    t.lt(135)
    t.fd(100*x)

def lt135_fd_longdiag():
    t.lt(150)
    t.fd(275)

def lt135_fd():
    t.lt(135)
    t.fd(100)

def lt60_fd():
    t.lt(75)
    t.fd(100)

rt120_fd()
lt120_fd()
rt90_fd()
rt90_fd()
lt120_fd()
lt120_fd()
lt75_fd_diag()
lt135_fd()
lt120_fd_diag()
lt60_fd()
lt135_fd_longdiag()

turtle.mainloop()