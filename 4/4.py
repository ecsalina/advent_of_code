
text = "".join(list(open("input.txt", "r")))


#part 1

digits = [str(i) for i in range(10)]
symbols = ['&', '+', '-', '/', '@', '#', '%', '*', '=', '$']

total = 0

value = None
posns = []
for posn, char in enumerate(text):
    if char in digits:
        if value is not None:
            value *= 10
            value += int(char)
        else:
            value = int(char)
        posns.append(posn)
    elif value is not None:
        #pinch off number and perform symbol check
        check_posns = [posns[0]-1, posns[0]-142, posns[0]+140, posns[-1]+1, posns[-1]-140, posns[-1]+142]
        check_posns += [posn+141 for posn in posns]
        check_posns += [posn-141 for posn in posns]
        for check_posn in check_posns:
            try:
                if text[check_posn] in symbols:
                    total += value
                    break
            except:
                continue
        value = None
        posns = []

print(total)
