def makeChocolate(small, big, goal):
	
	"""
	We want to make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can’t be done.
	makeChocolate(int small, int big, int goal)
	Examples:
	makeChocolate(4, 1, 9) -> 4
	makeChocolate(4, 1, 10) -> -1
	makeChocolate(4, 1, 7) -> 2
	"""

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