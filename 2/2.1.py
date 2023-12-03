#Could also do the below using a single regex, but it is more pythonic to be
#explicit, and it is more pythonic to use actual python (regex essentially
#being its own separate language)

file = open("input.txt", "r")
total = 0
for line in file:
    game = {}
    header, subsets = line.strip().split(":")
    game_id = int(header.split(" ")[1])
    game = {"red": 0, "green": 0, "blue": 0}
    for subset in subsets.split(";"):
        for block in subset.split(","):
            block_num, block_color = block[1:].split(" ")
            game[block_color] = max(int(block_num), game[block_color])
    if game["red"] <= 12 and game["blue"] <= 14 and game["green"] <= 13:
        total += game_id

print(total)
