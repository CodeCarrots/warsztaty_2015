# matematyka

## kilka "zewnętrznych" rzeczy

from math import sin, cos
import turtle

## tu zaczyna sie nasz kod do poprawienia

dex = []

val_a = -100
dex.append((val_a, val_a * sin(val_a) + cos(val_a)))
val_b = -90
dex.append((val_b, sin(val_b) + val_b * cos(val_b)))
val_c = -80
dex.append((val_c, val_c * sin(val_c) + cos(val_c)))
val_d = -70
dex.append((val_d, sin(val_d) + val_d * cos(val_d)))

val_a = 10
dex.append((val_a, val_a * sin(val_a) + cos(val_a)))
val_b = 20
dex.append((val_b, sin(val_b) + val_b * cos(val_b)))
val_c = 30
dex.append((val_c, val_c * sin(val_c) + cos(val_c)))
val_d = 40
dex.append((val_d, sin(val_d) + val_d * cos(val_d)))

val_a = 70
dex.append((val_a, val_a * sin(val_a) + cos(val_a)))
val_b = 80
dex.append((val_b, sin(val_b) + val_b * cos(val_b)))
val_c = 90
dex.append((val_c, val_c * sin(val_c) + cos(val_c)))
val_d = 100
dex.append((val_d, sin(val_d) + val_d * cos(val_d)))

## tu kończy się nasz kod do poprawienia

## to poniżej służy tylko do wyświetlenia wyników obliczeń

turtle.delay(0)
tt = turtle.Turtle()
tt.speed(0)
tt.penup()
tt.goto(dex[0])
tt.pendown()
for point in dex:
    tt.goto(point)
input('Enter/Ctrl+C to close')
