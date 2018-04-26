print('Input the number of grids to be printed')

number = input()
nn = int(number)

a = '+'
b = '-'
c = '|'
d = ' '

def plus_minus():
   first = a + b*4
   print(first * nn + '+')

def pipe():
    next = c + d*4
    print(next * nn + c)

for i in range(1,nn+1):
    plus_minus()
    for i in range(1,5):
        pipe()

plus_minus()
