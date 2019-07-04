# Supposes an individual is living in a perfectly grid/block like city, what is the longest random walk that 
# can be taken so that on average the individual will end up 4 blocks or fewer from home?

import random
def random_walk(n):
	"""Return coordinates after a walk of n blocks"""
	x, y = 0, 0
	for i in range(n):
		step = random.choice(['N', 'S', 'E', 'W'])
		if step == 'N':
			y += 1
		if step == 'S':
			y -= 1
		if step == 'E':
			x += 1
		if step == 'W':
			x -= 1
	return (x, y)

number_of_walks = 20000

for walk_length in range(1, 31):
	four_blocks = 0 # Number of walks 4 or fewer blocks from home
	for i in range(number_of_walks):
		(x, y) = random_walk(walk_length)
		distance = abs(x) + abs(y)
		if distance <= 4:
			four_blocks += 1
	four_blocks_percentage = float(four_blocks) / number_of_walks
	print("Walk size = ", walk_length, " / Percentage 4 blocks or fewer = ", 100*four_blocks_percentage)
