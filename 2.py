import turtle

t = turtle.Turtle()
t.shape('turtle')
t.speed(0)

def spiral(n: int, r: int, x: int = 0, y: int = 0, col: str = 'black'):
    t.up()
    t.goto(x, y)
    t.down()
    t.color(col)
    for i in range(n):
        t.circle(r)
        t.lt(360/n)

spiral(50, 100, 100, 100, 'red')
spiral(50, 100, 0, 0, 'blue')
