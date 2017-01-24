from collections import *
def ransom_note(magazine, rasom):
    dict_mag = Counter(magazine)
    dict_rason = Counter(rasom)
    
    return (dict_rason - dict_mag) == {}
    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"