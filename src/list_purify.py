def purify(lst):
    newlst = []
    for i in lst:
        if i % 2 == 0:
            newlst.append(i)
    return newlst