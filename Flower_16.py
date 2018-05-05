import turtle

flower_16 = turtle.Turtle()
print(flower_16)

for i in range(0,16):
    for i in range(0,18):
        flower_16.rt(2.5)
        flower_16.fd(10)

    flower_16.rt(157.5)

turtle.mainloop()