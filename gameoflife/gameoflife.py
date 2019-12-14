#!/usr/bin/env python

import unicornhat as unicorn
import time
import random
import numpy

unicorn.brightness(0.2)

board = numpy.zeros((8,8), dtype=numpy.byte)
color = [255, 255, 0]

def initialize(board):
	#initialize random number generator
	random.seed(time.time())
	#loop board
	for y in range(8):
		for x in range(8):
			#set element randomized
			rand = random.randint(0,1)
			board[x][y] = rand

def draw(board):
	for y in range(8):
		for x in range(8):
			#set pixel with color or unset it
			if board[x][y] == 1:
				unicorn.set_pixel(x,y,color[0],color[1],color[2])
			else:
				unicorn.set_pixel(x,y,0,0,0)
	#draw whole unicorn led matrix
	unicorn.show()

def compute(board):
	#game of live logic
	xmax, ymax = board.shape
    	b = board.copy()
    	for x in range(xmax):
        	for y in range(ymax):
            		n = numpy.sum(board[max(x - 1, 0):min(x + 2, xmax), max(y - 1, 0):min(y + 2, ymax)]) - board[x, y]
            		if board[x, y]:
                		if n < 2 or n > 3:
                    			b[x, y] = 0
            		elif n == 3:
                		b[x, y] = 1
	return b

initialize(board)
while True:
	draw(board)
	board = compute(board)
	time.sleep(1.5)
