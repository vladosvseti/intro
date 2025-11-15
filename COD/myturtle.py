from time import sleep
from turtle import *
def kvad(a, b="", fill=False):
	if b == "":
		b=a
	if not fill == False:
		begin_fill()
	for i in range(2):
		fd(a)
		left(90)
		fd(b)
		left(90)
	if not fill == False:
		end_fill()
def figur(a, b, fill=False):
	if not fill == False:
		begin_fill()
	for i in range(b):
		fd(a)
		left(360/b)
	if not fill == False:
		end_fill()
def circle2(a, fill=False):
	if not fill == False:
		begin_fill()
	circle(a)
	if not fill == False:
		end_fill()
def goto2(a, b, fill=False):
	if not fill == False:
		up()
	goto(a, b)
	if not fill == False:
		down()
