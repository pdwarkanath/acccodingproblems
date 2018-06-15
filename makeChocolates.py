def makeChocolate(small, big, goal):
	if goal > 5*big:
		newGoal = goal - (5*big)
	else:
		newGoal = goal % 5
	if newGoal > small:
		return -1
	else:
		return newGoal


print(makeChocolate(4, 1, 9))
print(makeChocolate(4, 1, 10))
print(makeChocolate(4, 1, 7))
print(makeChocolate(4, 1, 3))