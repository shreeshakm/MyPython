
a = '*'
b = ' '
x = 50

for i in range(0,10):
    print(b.center(x) + a*i + a + a*i)
    x = x - 1