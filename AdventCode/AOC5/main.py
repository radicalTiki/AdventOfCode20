# The first 7 characters will either be F or B;
# these specify exactly one of the 128 rows on the plane (numbered 0 through 127).
# Each letter tells you which half of a region the given seat is in.
# Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63)
# or the back (64 through 127). The next letter indicates which half of that region the seat is in,
# and so on until you're left with exactly one row.

# F means "front", B means "back", L means "left", and R means "right".

# The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane
# (numbered 0 through 7). The same process as above proceeds again, this time with only three steps.
# L means to keep the lower half, while R means to keep the upper half.

# Seat ID = row * 8 + column
# What is the highest seat ID on a boarding pass?

# Part 2
# Ding! The "fasten seat belt" signs have turned on. Time to find your seat.
# It's a completely full flight, so your seat should be the only missing boarding pass in your list.
# However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft,
# so they'll be missing from your list as well.
#
# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

rows = 127
columns = 7
seat_id_multi = 8


def traverse(trav_list):
    highest_value = 0
    all_seats = []

    for entry in trav_list:
        current_row = 0, rows
        current_column = 0, columns

        for char in entry[:7]:
            current_row = get_value(char, current_row)
        for char in entry[7:]:
            current_column = get_value(char, current_column)
        value = current_row * seat_id_multi + current_column
        all_seats.append([current_row, current_column, value])
        #
        # if highest_value < value:
        #     highest_value = value
    sorted_seats = sorted(all_seats, key=lambda tup: (tup[0], tup[1]))
    missing_seat = get_missing_seat(sorted_seats)
    return missing_seat
    # return highest_value


def get_missing_seat(seats):
    prev_id = seats[0]
    for seat in seats[1:]:
        if seat[2] == prev_id[2] + 1:
            prev_id = seat
        else:
            return seat[2] - 1

    return 1


def get_value(char, current_value):
    if abs(current_value[1] - current_value[0]) == 1:
        return current_value[1] if char == 'B' or char == 'R' else current_value[0]
    if char == 'F' or char == 'L':
        return current_value[0], int((current_value[1] + current_value[0]) / 2)
    else:
        return int((current_value[0] + current_value[1]) / 2) + 1, current_value[1]


if __name__ == '__main__':
    input_lines = open('input.txt').readlines()
    entries = [x.strip() for x in input_lines]

    answer = traverse(entries)

    print("answer: ", answer)
