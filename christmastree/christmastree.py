#!/usr/bin/env python

import unicornhat as unicorn

unicorn.brightness(1.0)

board = [[0,0,0,0,0,0,0,0],
	 [0,1,1,0,0,0,0,0],
         [0,1,1,1,1,0,0,0],
         [0,1,1,1,1,1,1,0],
         [1,1,1,1,1,1,1,1],
         [0,1,1,1,1,1,1,0],
         [0,1,1,1,1,0,0,0],
         [0,1,1,0,0,0,0,0]]
color_green = [2,97,0]
color_brown = [142,127,67]

def draw(board):
	for y in range(8):
		for x in range(8):
			#set pixel with color or unset it
			if board[x][y] == 1:
				if y != 0:
					unicorn.set_pixel(x,y,color_green[0],color_green[1],color_green[2])
				else:
					unicorn.set_pixel(x,y,color_brown[0],color_brown[1],color_brown[2])
	#draw whole unicorn led matrix
	unicorn.show()

while True:
	draw(board)
