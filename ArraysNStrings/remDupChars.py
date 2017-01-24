# Step 1: Resolving ambiguity
'''
Does string contains only Aschii characters?
is space also considered duplicate char?
'''

# Step 2: Design Algorithm
'''
1. Iterate through each char in string
2. Append to new list if not exist else continue
'''

# Step 3: Code
def rumDupChar(s):
        if s == None:
                return s

	newList = []
	i = 0
	while i < len(s):
		if s[i] not in newList:
			newList.append(s[i])
		i+=1
	
	return ''.join(c for c in newList)

# test cases:
rumDupChar('abc') #abc
rumDupChar('abbc') #abc
rumDupChar('') #
rumDupChar('dft123') #dft123
rumDupChar('dd333#$%') #d3#$%
