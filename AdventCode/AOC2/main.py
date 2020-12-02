entries = open('input.txt').readlines()
entries = [x.strip() for x in entries]


def traverse(trav_entries):
    valid = 0
    for entry in entries:
        low, high = get_low_high(entry)
        character = get_character(entry)
        if low <= entry.split(":")[1].count(character) <= high:
            valid += 1
    return valid


def get_low_high(entry):
    low_high = entry.split(" ")[0]
    low_high = low_high.split("-")
    return int(low_high[0]), int(low_high[1])


def get_character(entry):
    character = entry.split(" ")[1]
    return character[0]


if __name__ == '__main__':
    answer = traverse(entries)
    print("The answer = " + str(answer))
