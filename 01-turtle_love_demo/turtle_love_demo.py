import turtle


def draw_arc(r=1, angle=200):
    """
    绘画角度为angle步长为r的圆弧
    :return:
    """
    for i in range(angle):
        t.right(1)
        t.forward(r)


def draw_love():
    """
    绘画爱心
    :return:
    """
    t.color('red', 'pink')
    t.pensize(2)
    t.speed('fastest')
    t.goto(0, 0)
    t.begin_fill()  # 开始填充
    t.left(140)
    t.forward(112)
    draw_arc()
    t.left(120)
    draw_arc()
    t.forward(112)
    t.end_fill()  # 结束填充


def draw_name():
    """
    绘画字母
    :return:
    """
    t.speed('slow')
    t.pensize(3)
    t.up()
    # L顶点
    t.goto(-50, 122.7)
    if Name[0] == 'L':
        t.left(50)
        t.down()
        t.forward(40)
        t.left(90)
        t.forward(15)

    t.up()
    t.goto(-7.5, 122.7)
    if Name[1] == 'B':
        t.right(90)
        t.down()
        # 往下竖直
        t.forward(40)
        t.up()
        t.goto(-7.5, 122.7)
        t.left(90)
        t.down()
        draw_arc(r=0.19, angle=180)
        t.setheading(0)
        draw_arc(r=0.19, angle=180)

    t.up()
    # J顶点
    t.goto(37.5, 122.7)
    if Name[2] == 'X':
        t.setheading(0)  # 调整朝向为水平
        t.right(69.44)
        t.down()
        t.forward(43)
        t.up()
        t.goto(52.5, 122.7)
        t.setheading(0)  # 调整朝向为水平
        t.right(110.56)
        t.down()
        t.forward(43)
        t.up()
    t.goto(100, -10)
    t.write("I Like you")


Name = ['L', 'B', 'X']
t = turtle.Turtle()
draw_love()
draw_name()
turtle.mainloop()