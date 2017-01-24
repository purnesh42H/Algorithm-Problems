# Key Points/Assumptions:
'''
'''

# Algorithm:
'''
1. Convert string to list
2. if encounter space replace space by '%20' and continue till end of string.
'''

# Code:
def isExist(lst, sIndex, word):
    cur = sIndex
    wI = 0
    while wI < len(word):
        if cur >= len(lst) or lst[cur] != word[wI]:
            return False

        wI += 1
        cur +=1
        
    return True

def pullBack(lst, sIndex):
    cur = sIndex
    while cur < len(lst) - 1:
        lst[cur] = lst[cur + 1]
        cur += 1
        
    return lst[:-1]

def pushBack(lst, sIndex):
    cur = len(lst) - 1
    lst.append(lst[-1])
    while cur > sIndex:
        lst[cur] = lst[cur-1]
        cur -= 1
        
    return lst

def replaceBy(s, word1, word2):
    lst = list(s)
    sIndex = 0
    while sIndex < len(lst):
        if isExist(lst, sIndex, word1):
            word2Index = 0
            for c in word1:
                if word2Index >= len(word2):
                    lst = pullBack(lst, sIndex)
                else:
                    lst[sIndex] = word2[word2Index]
                    word2Index += 1
                sIndex += 1
                
            while word2Index < len(word2):
                lst = pushBack(lst, sIndex)
                lst[sIndex] = word2[word2Index]
                sIndex += 1
                word2Index += 1
                
        else:
            sIndex += len(word1)

    return ''.join(ch for ch in lst)

def urlify(s):
    return replaceBy(s,' ','%20')


# Tests:
'''
1. s = 'abn fe' will be 'abn%20fe'
'''

#Problems/bottlenecks:
'''
3 functions:
1. isExist
2. Pullback
3. Pushback
'''
