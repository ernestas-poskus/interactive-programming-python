def count(sequence, item):
    count = 0
    for w in sequence:
        if w == item:
            count += 1
    return count