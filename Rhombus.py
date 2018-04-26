
import turtle

rhombus = turtle.Turtle()
print(rhombus)

rhombus.lt(45)
rhombus.fd(100)
for i in range(0,3):
    rhombus.rt(90)
    rhombus.fd(100)

turtle.mainloop()
