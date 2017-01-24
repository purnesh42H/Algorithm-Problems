from math import *

def printInst(word):
	outputStr = []
	srow, scol = 1, 1
	for c in word:
		pos = ord(c) - ord('a') + 1
		row = int(ceil(float(pos) / 3))
		col = pos % 3
		if col == 0:
			col = 3
		srow, scol = output(outputStr, srow, scol, row, col)

	return ', '.join(w for w in outputStr)

def output(outputStr, srow, scol, drow, dcol):
	while srow != drow:
		if srow > drow:
			srow -= 1
			outputStr.append('up')
		else:
			srow += 1
			outputStr.append('down')

	while scol != dcol:
		if scol > dcol:
			scol -= 1
			outputStr.append('left')
		else:
			scol += 1
			outputStr.append('right')

	outputStr.append('PRESS')
	return srow, scol
