#Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

entries = open('input.txt').readlines()

answer = 0
entries = [x.strip() for x in entries]

for entry in entries:
    for entry2 in entries[1:]:
        for entry3 in entries[2:]:
            if int(entry) + int(entry2) + int(entry3) == 2020:
                answer = int(entry) * int(entry2) * int(entry3)
                break
        if answer != -0:
            break
    if answer != 0:
        break

print("The answer = " + str(answer))
