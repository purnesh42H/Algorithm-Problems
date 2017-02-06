#!/bin/python

import sys

def isMatrixMatch(mat1, mat2, r, c, j):
    for i in range(r):
        temp = mat1[i][j:j+c]
        if temp != mat2[i]:
            return False
        
    return True

t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)
        
    i = 0
    j = 0
    found = False
    while i <= R - r and found == False:
        j=0
        mat1 = G[i:i+r]
        while j <= C - c and found == False:
            if isMatrixMatch(mat1, P, r, c, j):
                found = True
            j+=1
        i+=1
       
    if found:
        print 'YES'
    else:
        print 'NO'
