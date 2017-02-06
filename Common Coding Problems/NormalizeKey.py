def normalize(key, k = 0):
    revKey = key[::-1]
    lstKey = revKey.split('-')
    output = []
    splits = len(lstKey)
    nIndex = 0
    if k == 0:
        k = len(revKey.strip('-'))/len(lstKey)
    while nIndex < splits - 1:
        if len(lstKey[nIndex]) >= k:
            output.append(lstKey[nIndex][:k])
            lstKey[nIndex + 1] = lstKey[nIndex][k:] + lstKey[nIndex + 1]
        else:
            take = k - len(lstKey[nIndex])
            output.append(lstKey[nIndex] + lstKey[nIndex+1][:take])
            lstKey[nIndex + 1] = lstKey[nIndex+1][take:]

        nIndex += 1

    output.append(lstKey[nIndex])

    return '-'.join(i[::-1] for i in output[::-1])


print normalize('1234-343-9087')
