import turtle, random

turtle.bgcolor('black')

colors = ['red', 'skyblue', 'yellow', 'white', 'aqua', 'cyan']
t = turtle.Turtle()
t.speed(0)
t.shape('turtle')

# 사각형
def square(d: int, r: int):
    for i in range(r):
        for i in range(4):
            t.fd(d)
            t.lt(360/4)
        t.lt(360/r)

# 원
def circle(d: int, r: int):
    for i in range(r):
        t.circle(d)
        t.lt(360/r)

# 삼각형
def triangle(d: int, r: int):
    for i in range(r):
        for i in range(3):
            t.fd(d)
            t.lt(360/3)
        t.lt(360/r)
    

# 움직임
def move():
    t.up()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.down()

def newFire(type: int):
    t.color(colors[random.randint(0, (len(colors) - 1))])
    for i in range(3):
        d = random.randint(30, 100)
        if type == 1:
            square(d + (i*30), random.randint(10, 30))
        elif type == 2:
            circle(d + (i*10), random.randint(20, 50))
        elif type == 3:
            triangle(d + (i*20), random.randint(20, 40))

for i in range(5):
    move()
    newFire(random.randint(1, 3))



