from collections import *
def ransom_note(magazine, rasom):
    dict_mag = Counter(magazine)
    dict_rason = Counter(rasom)
    if len(dict_rason) > len(dict_mag):
        return False
    for word in dict_rason:
        if word not in dict_mag:
            return False
        if dict_mag[word] < dict_rason[word]:
            return False
    
    return True
    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"