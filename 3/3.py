import re

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
    if char not in digits:
        if value is None:
            continue
        else:
            #pinch off number and perform symbol check
            check_posns = [posns[0]-1, posns[0]-142, posns[0]+140, posns[-1]+1, posns[-1]-140, posns[-1]+142]
            check_posns += [posn+141 for posn in posns]
            check_posns += [posn-141 for posn in posns]
            for check_posn in check_posns:
                try:
                    if text[check_posn] in symbols:
                        total += value
                        value = None
                        posns = []
                        break
                except:
                    continue
            #no break
            value = None
            posns = []

print(total)


#part 2

gears = {}
ratios = 0

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
    if char not in digits:
        if value is None:
            continue
        else:
            #pinch off number and perform symbol check
            check_posns = [posns[0]-1, posns[0]-142, posns[0]+140, posns[-1]+1, posns[-1]-140, posns[-1]+142]
            check_posns += [posn+141 for posn in posns]
            check_posns += [posn-141 for posn in posns]
            for check_posn in check_posns:
                try:
                    if text[check_posn] == "*":
                        if check_posn in gears:
                            ratios += gears[check_posn]*value
                            print(ratios)
                        else:
                            gears[check_posn] = value
                        value = None
                        posns = []
                        break
                except:
                    continue
            #no break
            value = None
            posns = []

print(ratios)




