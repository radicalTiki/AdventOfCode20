# The form asks a series of 26 yes-or-no questions marked a through z.
# All you need to do is identify the questions for which anyone in your group answers "yes".
# For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

def coalesce_questions(check):
    group_questions = []
    coalesce = []
    person_count = 0
    for entry in check:
        if entry == '':
            # new line add questions to group questions
            group_questions.append([coalesce, person_count])
            coalesce = []
            person_count = 0
        else:
            person_count += 1
            for item in entry:
                coalesce.append(item)
    return group_questions


def get_question_count(groups_check):
    count = 0
    for group in groups_check:
        count += len("".join(set(group)))

    return count


def get_all_question_count(groups_check):
    count = 0
    for group in groups_check:
        for char in "".join(set(group[0])):
            if group[0].count(char) == group[1]:
                count += 1
    return count


if __name__ == '__main__':
    input_lines = open('input.txt').readlines()
    entries = [x.strip() for x in input_lines]
    groups = coalesce_questions(entries)
    # answer = get_question_count(groups)
    answer = get_all_question_count(groups)
    print("answer: ", answer)
