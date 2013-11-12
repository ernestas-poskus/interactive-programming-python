def censor(text, word):
    lst = text.split()
    for w in lst:
        if w == word:
            lst[lst.index(w)] = len(w) * '*'

    return " ".join(lst)
            
print censor('hey hey afwaf', 'hey')