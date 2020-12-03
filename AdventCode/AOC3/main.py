# # You start on the open square (.) in the top-left corner and need to reach the bottom
# # (below the bottom-most row on your map).
# # The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers);
# # start by counting all the trees you would encounter for the slope right 3, down 1:
# # From your starting position at the top-left, check the position that is right 3 and down 1.
# # Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.
# # The locations you'd check in the above example are marked here with O where there was an open square and X
# # where there was a tree:
# #280

import math

tree = '#'


def traverse1(trav_entries, pos_x, pos_y):
    trees_hit = 0
    current_pos = 0
    for entry in entries[pos_y::pos_y]:
        current_pos = current_pos + pos_x
        if entry[current_pos % len(entry)] == tree:
            trees_hit = trees_hit + 1
    return trees_hit


if __name__ == '__main__':
    entries = open('input.txt').readlines()
    entries = [x.strip() for x in entries]

    answers = [traverse1(entries, 1, 1)]
    print("1:1 : ", answers[-1])

    answers.append(traverse1(entries, 3, 1))
    print("3:1 : ", answers[-1])

    answers.append(traverse1(entries, 5, 1))
    print("5:1 : ", answers[-1])

    answers.append(traverse1(entries, 7, 1))
    print("7:1 : ", answers[-1])

    answers.append(traverse1(entries, 1, 2))
    print("1:2 : ", answers[-1])
#
    print("answer: ", math.prod(answers))




# tree = '#'
# move_x = 3
#
#
# def traverse1(trav_entries):
#     trees_hit = 0
#     pos_x = 0
#     for entry in entries[1:]:
#         pos_x = pos_x + move_x
#         if entry[pos_x % len(entry)] == tree:
#             trees_hit = trees_hit + 1
#     return trees_hit
#
#
# if __name__ == '__main__':
#     entries = open('input.txt').readlines()
#     entries = [x.strip() for x in entries]
#     answer = traverse1(entries)
#     print("The answer = " + str(answer))
