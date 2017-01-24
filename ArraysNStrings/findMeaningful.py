def ngrams(word, n):
    ngrams = []
    i = 0
    while i + n <= len(word):
        ngrams.append(word[i:i+n])
        i += 1

    return ngrams
