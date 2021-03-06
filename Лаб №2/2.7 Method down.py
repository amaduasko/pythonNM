import math

NN = 7
a = 1
b = 0.5
c = -1
d = -1
e = 1
f = -2
g = 1
h = 0

def f1(x, y):
  return math.sin(a*x + b) + c*y + d
def f2(x, y):
  return math.cos(e*y + f) + g*x + h

def F(x,y):
  return f1(x,y)*f1(x,y) + f2(x,y)*f2(x,y)

def F_x(x,y):
  return 2*f1(x,y)*f1_x(x,y) + 2*f2(x,y)*f2_x(x,y)

def F_y(x,y):
  return 2*f1(x,y)*f1_y(x,y) + 2*f2(x,y)*f2_y(x,y)

def f1_x(x,y):
  return a*math.cos(a*x + b)
def f1_y(x,y):
  return c

def f2_x(x,y):
  return g
def f2_y(x,y):
  return -e*math.sin(e*y + b)

def G(x,y):
  return (-f1(x,y)-f1_y(x,y)*H(x,y))/f1_x(x,y)

def H(x,y):
  return (-f2(x,y)*f1_x(x,y) + f2_x(x,y)*f1(x,y))/(f1_x(x,y)*f2_y(x,y)-f2_x(x,y)*f1_y(x,y))



x0 = 0.1
y0 = 0.1

eps=0.001
xn = x0 - a*F_x(x0,y0)
yn = y0 - a*F_y(x0,y0)
while(abs(xn - x0) > eps or abs(yn - y0) > eps):
  x0 = xn
  y0 = yn
  xn = x0 + G(x0,y0)
  yn = y0 + H(x0,y0)

print(xn, yn)
print(f1(xn, yn))
print(f2(xn, yn))