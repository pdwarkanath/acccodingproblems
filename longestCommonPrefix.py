def longestCommonPrefix(strs):
	prefix = strs[0]
	for i in range(len(strs)):
		for j in range(len(prefix)):
			try:
				if prefix[j] == strs[i][j]:
					continue
				else:
					prefix = prefix[0:j]
					if len(prefix) == 0:
						return ""
			except IndexError:
				prefix = prefix[0:j]
	return prefix

strs = ["prefix", "prefixjoe", "pre", "pref"]

print(longestCommonPrefix(strs))

