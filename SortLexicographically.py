# Enter your code here. Read input from STDIN. Print output to STDOUT
def findPivot(wordList):
    j = len(wordList) - 1
    while j > 0:
        if ord(wordList[j]) > ord(wordList[j-1]):
            return j-1
        j-=1
    
    return -1

def rightMostSuccessor(pivot, wordList):
    j = len(wordList) - 1
    while j > pivot:
        if ord(wordList[j]) > ord(wordList[pivot]):
            return j
        j-=1
    
    return 1

n = int(raw_input().strip())
    

for i in range(n):
    word = raw_input().strip()
    j=len(word) - 1
    newWord = list(word)
    pivot = findPivot(newWord)
    if pivot != -1:
        right = rightMostSuccessor(pivot, newWord)
        temp = newWord[pivot]
        newWord[pivot] = newWord[right]
        newWord[right] = temp
        newWord = newWord[:pivot+1] + sorted(newWord[pivot+1:])
        
    if ''.join(newWord) == word:
        print 'no answer'
    else:
        print ''.join(newWord)
