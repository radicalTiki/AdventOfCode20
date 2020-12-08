# acc increases or decreases a single global value called the accumulator by the value given in the argument.
# For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction,
# the instruction immediately below it is executed next.
# jmp jumps to a new instruction relative to itself.
# The next instruction to execute is found using the argument as an offset from the jmp instruction;
# for example, jmp +2 would skip the next instruction, jmp +1 would continue
# to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
# nop stands for No OPeration - it does nothing.
# The instruction immediately below it is executed next.

# Part 2
# Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
# What is the value of the accumulator after the program terminates?


def traverse_code(check, accumulator, used_index):
    pos = 0
    while pos not in used_index:
        if pos == len(check):
            return accumulator, pos
        entry = check[pos]
        code_split = entry.split(' ')
        if pos in used_index:
            return accumulator
        elif code_split[0] == 'jmp':
            used_index.append(pos)
            pos = int(find_next(pos + int(code_split[1]), check, used_index))

        value = get_value(pos, check, used_index)
        if value == -1:
            return accumulator, pos
        else:
            accumulator += value
        pos += 1

    return accumulator, pos


def change_one_check(change_list):
    changed_values = []
    for pos, value in enumerate(change_list):
        change_split = value.split(' ')
        if change_split[0] == 'nop' or change_split[0] == 'jmp':
            changed_values.append(pos)

    for change_value in changed_values:
        check_changed = change_list.copy()
        if check_changed[change_value].split(' ')[0] == 'nop':
            check_changed[change_value] = 'jmp ' + check_changed[change_value].split(' ')[1]
        else:
            check_changed[change_value] = 'nop ' + check_changed[change_value].split(' ')[1]
        accum, x = traverse_code(check_changed, 0, [])
        print(x, change_value)
        if x >= len(change_list):
            return accum, x


def get_value(index, check, used_index):
    if index in used_index:
        return -1
    code_split = check[index].split(' ')
    if code_split[0] == 'acc':
        used_index.append(index)
        return int(code_split[1])
    elif code_split[0] == 'nop':
        used_index.append(index)
        return 0


def find_next(index, check, used_index):
    if check[index].split(' ')[0] == 'jmp':
        used_index.append(index)
        return find_next(int(index) + int(check[index].split(' ')[1]), check, used_index)
    else:
        return index


if __name__ == '__main__':
    input_lines = open('input.txt').readlines()
    entries = [x.strip() for x in input_lines]
    # answer, pos = traverse_code(entries, 0, [])
    answer, pos = change_one_check(entries)
    print("answer: ", answer, pos)
