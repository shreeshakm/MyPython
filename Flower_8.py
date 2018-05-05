import turtle

test = turtle.Turtle()
print(test)

for i in range(0,8):
    for i in range(0,45):
        test.rt(2)
        test.fd(5)

    test.rt(135)

turtle.mainloop()
