def find_sum_pair(lst, N):
    """
    lst: list of sorted integers
    N: int

    Given a list of sorted integers, e.g. [1, 3, 5, 7], and an integer N, return true if there is a pair of integers in the list that sum up to N. If there is no pair, return false. 
    Examples:
    Input: [1, 2, 4, 5, 6], N = 8
    Output: true
    Input: [1, 1, 3, 4], N = 2
    Output: true
    Input: [3, 4, 7,  10], N = 0
    Output: false
    """
    # Get indices of first and last elements
    
    low = 0
    high = len(lst)-1
    
    test_sum = lst[low]+lst[high]
    
    while low < high:
        test_sum = lst[low]+lst[high]
        if test_sum == N:
            return True
        elif test_sum < N: # Move ahead from beginning of list
            low += 1
        elif test_sum > N: # Move back from end of list
            high -= 1
    return False
        

lst = [1, 2, 4, 5, 6]
N = 8

print(find_sum_pair(lst, N))
