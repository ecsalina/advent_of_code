
"""
Time:        54     70     82     75
Distance:   239   1142   1295   1253
"""

#part 1

races = [(54, 239), (70, 1142), (82, 1295), (75, 1253)]

num_combos = []
for max_time, record_distance in races:
    num_combos.append([])
    for i in range(max_time):
        distance = i*(max_time-i)
        if distance > record_distance:
            num_combos[-1].append(distance)

print(len(num_combos[0]) , len(num_combos[1]) , len(num_combos[2]), len(num_combos[3]))
print(len(num_combos[0]) * len(num_combos[1]) * len(num_combos[2]) * len(num_combos[3]))


#part 2

max_time = 54708275
record_distance = 239114212951253

for i in range(max_time):
    if i*(max_time-i) > record_distance:
        break

num_combos = max_time - 2*i + 1

print(num_combos)
