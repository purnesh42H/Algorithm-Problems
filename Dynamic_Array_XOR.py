# Enter your code here. Read input from STDIN. Print output to STDOUT

N, Q = raw_input().strip().split(' ')
seq = []

for n in range(int(N)):
    seq.append([])
    
lastAns  = 0
for q in range(int(Q)):
    opr, x, y  = raw_input().strip().split(' ')
    seqNo = (int(x) ^ lastAns) % int(N)
    if opr == '1':
        seq[seqNo].append(int(y))
    elif opr == '2':
        index = int(y) % len(seq[seqNo])
        lastAns = seq[seqNo][index]
        print lastAns
