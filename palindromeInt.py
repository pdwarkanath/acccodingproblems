import math

def getCleanInt(x):
	x = int(abs(x))
	
	return x



def getNoOfDigits(x):
	n = int(math.log10(x))+1
	
	return n

def isPalindrome(x):
	x = getCleanInt(x)
	n = getNoOfDigits(x)

	for i in range(n//2):
		if (x//(10**(n-i-1)))%10 == (x % (10**(i+1)))//(10**i):
			continue
		else:
			return False
	return True


print(isPalindrome(1234))
print(isPalindrome(-2721272))

