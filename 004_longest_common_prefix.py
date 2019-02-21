def longest_common_prefix(strs):
    """
    strs: list of strings
    
    Write a function to find the longest common prefix string amongst an array of strings. 
    Ex: 
    ['prefix', 'prefixjoe', 'pre', 'pref']
    Longest Common Prefix: 'pre'
    ['joe', 'bob', 'ryan']
    Longest Common Prefix: ''

    """
    if (strs is None) or len(strs) == 0:
        return ''
    
    min_str = min(strs, key = len)
    n = len(min_str)
    
    i = 0
    prefix = min_str[i]
    
    while i < n:
        for s in strs:
            if prefix[i] != s[i]:
                return prefix[:-1]
            else:
                continue
        i += 1
        try:
            prefix += min_str[i]
        except IndexError:
            return prefix
    
    return prefix


strs = ["prefix", "prefixjoe", "pre", "pref"]
print(longest_common_prefix(strs))

strs = ['joe', 'bob', 'ryan']
print(longest_common_prefix(strs))