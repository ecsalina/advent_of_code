#Could also do the below using a single regex, but it is more pythonic to be
#explicit, and it is more pythonic to use actual python (regex essentially
#being its own separate language)

file = open("input.txt", "r")
total = 0
for line in file:
    header, subsets = line.strip().split(":")
    game_id = int(header.split(" ")[1])
    game = {"red": 0, "green": 0, "blue": 0}
    for subset in subsets.split(";"):
        for block in subset.split(","):
            block_num, block_color = block[1:].split(" ")
            game[block_color] = max(int(block_num), game[block_color])
    total += game["red"] * game["blue"] * game["green"]

print(total)


#Using regex because why not
import re

file = open("input.txt", "r")

[re.match("Game (?<group_id>\d+):(();?)+
