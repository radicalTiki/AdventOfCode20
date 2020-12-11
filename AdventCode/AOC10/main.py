# Each of your joltage adapters is rated for a specific output joltage (your puzzle input).
# Any given adapter can take an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.
#
# In addition, your device has a built-in joltage adapter rated for 3 jolts higher
# than the highest-rated adapter in your bag. (If your adapter list were 3, 9, and 6,
# your device's built-in adapter would be rated for 12 jolts.)

# AoC day 10 part 2
from collections import Counter


def get_jolt_difference(sorted_jolts):
    jolt_diff1, jolt_diff2, jolt_diff3 = 0, 0, 0
    sorted_jolts.insert(0, 0)
    for index in range(1, len(sorted_jolts)):
        jolt = sorted_jolts[index]
        if jolt - sorted_jolts[index - 1] == 1:
            jolt_diff1 += 1
        elif jolt - sorted_jolts[index - 1] == 2:
            jolt_diff2 += 1
        elif jolt - sorted_jolts[index - 1] == 3:
            jolt_diff3 += 1

    return jolt_diff1, jolt_diff3


def get_jolt_groups(sorted_jolts):
    c = Counter({0: 1})
    for x in sorted_jolts:
        c[x + 1] += c[x]
        c[x + 2] += c[x]
        c[x + 3] += c[x]
    return c[max(sorted_jolts) + 3]


if __name__ == '__main__':
    input_lines = open('input.txt').readlines()
    entries = [int(x.strip()) for x in input_lines]
    entries.sort()
    answer = get_jolt_difference(entries)
    answer2 = get_jolt_groups(entries)
    print("answer: ", answer[0] * (answer[1] + 1))
    print("answer2: ", answer2)
