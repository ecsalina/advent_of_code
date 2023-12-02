#requires no library imports and is pythonic in construction

strs = list(open("input.txt", "r").readlines())

digits = set([str(i) for i in range(10)])
total = sum([i[0]*10+i[-1] if i else 0 for i in
    [[int(c) for c in s if c in digits] for s in strs]])

print(total)
