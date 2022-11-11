#!/usr/bin/env python3
# coding=utf-8

import turtle

bob = turtle.Turtle()


def draw_bob(left_or_right, angle, length):
    if left_or_right == "right":
        bob.right(angle)
    else:
        bob.left(angle)

    bob.forward(length)


def draw_turtle(left_or_right, angle, length):
    if left_or_right == "right":
        turtle.right(angle)
    else:
        turtle.left(angle)

    turtle.forward(length)
# Начинаем окрашивать фронтальную сторону коробки
bob.fillcolor("#C0C0C0")
bob.begin_fill()

# Начинаем построение фронтальной стороны коробки

draw_bob("left", 0, 75)
draw_bob("left", 90, 105)
draw_bob("left", 90, 75)
draw_bob("left", 90, 15)
bob.end_fill()

bob.fillcolor("#FFD700")
bob.begin_fill()
draw_bob("left", -90, 40)
draw_bob("left", 90, 25)
draw_bob("left", 90, 40)
draw_bob("left", -90, 25)
bob.end_fill()
bob.fillcolor("#FFD700")
bob.begin_fill()
draw_bob("left", -90, 40)
draw_bob("left", 90, 25)
draw_bob("left", 90, 40)
draw_bob("left", -90, 15)
bob.end_fill()
bob.fillcolor("#C0C0C0")
bob.begin_fill()
draw_bob("left", 90, 30)
draw_bob("left", -90, 25)
draw_bob("left", 90, 60)
draw_bob("left", 90, 15)
draw_bob("left", 90, 50)
draw_bob("left", -90, 10)
draw_bob("left", 90, 5)
draw_bob("left", -90, 30)
draw_bob("left", -90, 20)
draw_bob("left", 90, 60)
draw_bob("left", 90, 20)
draw_bob("left", 90, 60)
draw_bob("left", -90, 15)
draw_bob("left", -90, 60)
draw_bob("left", -90, 15)
draw_bob("left", 90, 15)
bob.end_fill()
bob.fillcolor("")
bob.begin_fill()
draw_bob("left", 90, 35)
draw_bob("left", 90, 105)
draw_bob("left", 90, 80)
bob.end_fill()
turtle.done()
