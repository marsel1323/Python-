# coding: utf-8

import turtle, random, math
import MrRobot

phi = 360 / 7
r = 50

def gotoxy(x,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()

def draw_circle(r, color):
	turtle.fillcolor(color)
	turtle.begin_fill()
	turtle.circle(r)
	turtle.end_fill()


turtle.speed(0)

def draw_pistol(base_x, base_y):
	# основной круг
	gotoxy(base_x, base_y)
	turtle.circle(80)
	# мушка
	gotoxy(base_x, base_y + 160)
	draw_circle(5, 'red')
	
	#барабан
	for i in range(0, 7):
		phi_rad = phi * i * math.pi / 180.0
		gotoxy(base_x + math.sin(phi_rad)*r, base_y + math.cos(phi_rad)*r + 60)
		draw_circle(22,'white')

def rotate_pistol(base_x, base_y, start):
	for i in range(start, random.randrange(7,100)):
		phi_rad = phi * i * math.pi / 180.0
		gotoxy(base_x + math.sin(phi_rad)*r, base_y + math.cos(phi_rad)*r + 60)
		draw_circle(22,'brown')
		draw_circle(22,'white')
			
	gotoxy(base_x + math.sin(phi_rad)*r, base_y + math.cos(phi_rad)*r + 60)
	draw_circle(22, 'brown')
	
	return i % 7	
	
draw_pistol(100, 100)
			
answer = ''
start = 0
while answer != 'N':
	answer = turtle.textinput("Play?", "Y/N")
	
	if answer == 'Y':
		start = rotate_pistol(100, 100, start)			
		
		start = 0
		if start == 0:
			gotoxy(-50,250)
			turtle.write("You lose!", font=("Arial", 18, "normal"))
			
			z = random.randrange(0, 3)
			if z == 0:
				MrRobot.duble_files('test')
			elif z == 1:
				MrRobot.random_delete('test')
			else:
				gotoxy(-100, -50)
				turtle.write("You're lucky!", font=("Arial", 20, "normal"))
	else:
		pass
