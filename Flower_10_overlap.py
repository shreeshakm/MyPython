import turtle

test = turtle.Turtle()
print(test)

def petal():
    for i in range (0,2):
         for i in range(0,60):
            test.fd(5)
            test.rt(0.5)
         test.rt(150)

def flower():
    for i in range(0,10):
        petal()
        test.rt(36)
flower()

turtle.mainloop()
