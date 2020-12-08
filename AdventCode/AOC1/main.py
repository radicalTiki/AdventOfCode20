# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

entries = open('input.txt').readlines()

answer = 0
entries = [x.strip() for x in entries]


def traverse(trav_entries):
    for entry in trav_entries:
        for entry2 in trav_entries[1:]:
            for entry3 in trav_entries[2:]:
                if int(entry) + int(entry2) + int(entry3) == 2020:
                    return int(entry) * int(entry2) * int(entry3)


if __name__ == '__main__':
    answer = traverse(entries)
    print("The answer = " + str(answer))
