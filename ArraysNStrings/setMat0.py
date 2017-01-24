# Step 1: Ambiguity:
'''
1. can we return a new matrix? or we have to do in place?
2. does matrix contain all integers?
'''

# Step 2: Algorithm
'''
1. Keep track of which row has 0
2. Two arrays keeping track of which row and column has 0
3. Set element as 0 if its row or column has 0
'''	

	
def setRCZero(mat):
        rows = []
	for x in range(len(mat)):
                rows.append(0)
	cols = []
	for x in range(len(mat[0])):
                cols.append(0)
	i = 0
	while i < len(mat):
		j = 0
		while j < len(mat[i]):
			if mat[i][j] == 0:
                                rows[i] = 1
                                cols[j] = 1
			j += 1
		i += 1

	i = 0
	while i < len(mat):
		j = 0
		while j < len(mat[i]):
			if rows[i] == 1 or cols[j] == 1:
				mat[i][j] = 0
			j += 1
		i += 1

	return mat
						
		
