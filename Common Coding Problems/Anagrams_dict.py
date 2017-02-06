def getFrequency(string):
    s_index = 0
    dict_s = {}
    while s_index < len(string):
        key = string[s_index]
        if key in dict_s:
            dict_s[key] += 1
        else:
            dict_s[key] = 1
        s_index += 1
    return dict_s

def getDelCount (dict1, dict2):
    delCount = 0
    for character in dict1:
        if character in dict2:
            if dict1[character] >  dict2[character]:
                delCount += dict1[character] - dict2[character]
        else:
            delCount += dict1[character]
    return delCount

def number_needed(a, b):
    a_dict = getFrequency(a)
    b_dict = getFrequency(b)
    
    delCount = getDelCount(a_dict,b_dict) + getDelCount(b_dict,a_dict)
    
    return delCount

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)