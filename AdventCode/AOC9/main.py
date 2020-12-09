# XMAS starts by transmitting a preamble of 25 numbers.
# After that, each number you receive should be the sum of any two of the 25 immediately previous numbers.
# The two numbers will have different values, and there might be more than one such pair.

# The first step of attacking the weakness in the XMAS data is to find the first number in the list
# (after the preamble) which is not the sum of two of the 25 numbers before it.
# What is the first number that does not have this property?

# Step 2
# The final step in breaking the XMAS encryption relies on the invalid number you just found:
# you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

# To find the encryption weakness, add together the smallest and largest number in this contiguous range;
# in this example, these are 15 and 47, producing 62.

# preamble_num = 25
check_value = 1038347917
preamble_num = 5
# check_value = 127


def find_first_non_sum(check_list, current_index):
    value_check = int(check_list[current_index])
    sliced_list = check_list[current_index - preamble_num:current_index:]
    for pos, value in enumerate(sliced_list):
        for pos2, value2 in enumerate(sliced_list[1:]):
            check_sum = int(value) + int(value2)
            if check_sum == value_check:
                return find_first_non_sum(check_list, current_index + 1)
    return current_index


def find_two_consecutive(check_list):
    for pos, value in enumerate(check_list):
        check_sum = int(value)

        for pos2, value2 in enumerate(check_list[pos + 1:]):
            check_sum += int(value2)
            if check_sum == check_value:
                return max(check_list[int(pos):int(pos + pos2 + 2)]), min(check_list[int(pos):int(pos + pos2 + 2)])
            elif check_sum > check_value:
                break


if __name__ == '__main__':
    input_lines = open('input.txt').readlines()
    entries = [x.strip() for x in input_lines]
    # answer = entries[find_first_non_sum(entries, preamble_num)]
    max, min = find_two_consecutive(entries)
    print("answer: ", int(max) + int(min))
