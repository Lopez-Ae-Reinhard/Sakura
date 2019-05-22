import turtle
import time

boxsize = 200
caught = False
score = 0


# 定义响应键盘消息的函数
def up():
    mouse.forward(10)
    checkbound()


def left():
    mouse.left(45)


def right():
    mouse.right(45)


def back():
    mouse.backward(10)
    checkbound()


def quitTurtles():
    window.bye()


# 检测边界
def checkbound():
    global boxsize  # 使用外部变量
    if mouse.xcor() > boxsize:
        mouse.goto(boxsize, mouse.ycor())
    if mouse.xcor() < -boxsize:
        mouse.goto(-boxsize, mouse.ycor())
    if mouse.ycor() > boxsize:
        mouse.goto(mouse.xcor(), boxsize)
    if mouse.ycor() > -boxsize:
        mouse.goto(mouse.xcor(), -boxsize)


# 设置屏幕
window = turtle.Screen()
mouse = turtle.Turtle()
cat = turtle.Turtle()
mouse.penup()
mouse.penup()
mouse.goto(100, 100)

# 添加对键盘消息的监听
window.onkeypress(up, "Up")
window.onkeypress(left, "Left")
window.onkeypress(right, "Right")
window.onkeypress(back, "Down")
window.onkeypress(quitTurtles, "Escape")
# 定义难度系数
difficulty = window.numinput("Difficulty", "Enter a difficulty from easy (1),for hard (5)", minval=1, maxval=5)

window.listen()
# 主循环
while not caught:
    cat.setheading(cat.towards(mouse))
    cat.forward(8 + difficulty)
    score = score + 1
    if cat.distance(mouse) < 5:  # 猫和老鼠的距离小于5个像素，表示老鼠被毛抓住了
        caught = True
    time.sleep(0.2 - (0.01 * difficulty))
window.textinput("Game Over", "Well Done.You scored: " + str(score * difficulty))
window.bye()