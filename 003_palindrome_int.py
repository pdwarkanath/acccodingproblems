def palindrome_int(x):
    """
    
    Determine whether an integer is a palindrome. Do this without extra space.

    Hints:
    Could negative integers be palindromes? (ie, -1)
    If you are thinking of converting the integer to string, note the restriction of using extra space.
    You could also try reversing an integer. However, the reversed integer might overflow. How would you handle such case?
    There is a more generic way of solving this problem.

    
    """
    reverse_num = 0
    while x > reverse_num:
        reverse_num = reverse_num*10 + x%10
        x = x//10
    return x == reverse_num or x == reverse_num//10



print(isPalindrome(1234))
print(isPalindrome(-2721272))

