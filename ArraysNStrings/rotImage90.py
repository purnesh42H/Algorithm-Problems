# Key Points/Assumptions:
'''
1. Which rotation? Clockwise
2. What does matrix contain? characters?, integers? - No info
'''

#Example:
'''
[1,2]
[3,4]
=>
[3,1]
[4,2]

[1,2,3]
[4,5,6]
[7,8,9]
=>
[7,4,1]
[8,5,2]
[9,6,3]
'''

# Algorithm:
'''
1. We can rotate layers starting from outermost to innermost
2. Layer rotation
    1. Swap corners of adjacent edges 
    2. Swap inner cells of adjacent edges

[1,2,3] 
[4,5,6] 
[7,8,9]
=>
[1,2,3]
[4,0,6] 
[7,8,9]
=>
[7,2,1]
[4,5,6] 
[9,8,3]
=>
[7,4,1]
[8,5,2] 
[9,6,3]
=>
[7,4,1]
[8,5,2] 
[9,6,3]
'''

#Code
def rotMat(mat):
    layer = 0
    n = len(mat)
    while layer < n/2:
        row = 0
        while row < len(mat) - 1 - layer:
            temp = mat[layer][layer + row]
            mat[layer][layer + row] = mat[n - 1 - layer - row][layer]
            mat[n - 1 - layer - row][layer] = mat[n - 1 - layer][n-1-layer-row]
            mat[n - 1 - layer][n-1-layer-row] = mat[layer+row][n-1-layer]
            mat[layer+row][n-1-layer] = temp
            row += 1

        layer += 1

    return mat


# Test:
'''
[1,2,3,10] 
[4,5,6,11]
[13,14,15,16]
[7,8,9,12]
=>
[1,2,3,10] 
[4,0,0,11]
[13,0,0,16]
[7,8,9,12]
=>
[7,2,3,1] 
[4,0,0,11]
[13,0,0,16]
[12,8,9,10]
=>
[7,13,3,1] 
[4,0,0,2]
[9,0,0,16]
[12,8,11,10]
=>
[7,13,4,1] 
[8,0,0,2]
[9,0,0,3]
[12,16,11,10]
=>
[7,13,4,1] 
[8,0,0,2]
[9,0,0,3]
[12,16,11,10]
'''
