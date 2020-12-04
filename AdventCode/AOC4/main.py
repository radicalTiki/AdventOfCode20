# The automatic passport scanners are slow because they're having trouble detecting which passports
# have all required fields. The expected fields are as follows:
#
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) -> optional

# Passport data is validated in batch files (your puzzle input).
# Each passport is represented as a sequence of key:value pairs separated by spaces or newlines.
# Passports are separated by blank lines.

# PART 2
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


import re


def coalesce_passports(check):
    passports_coalesce = []
    coalesce = []
    for entry in check:
        if entry == '':
            # new line add passport to passports and clear
            passports_coalesce.append(coalesce)
            coalesce = []
        else:
            for item in entry.split(' '):
                coalesce.append(item)
    return passports_coalesce


def check_passports(passports_check):
    total = 0
    for passport in passports_check:
        count = 0
        if len(passport) >= 7:
            for key, value in [entry.split(":") for entry in passport]:
                if key != 'cid':
                    count = count + 1
        if count == 7:
            if check_valid(passport):
                total = total + 1
    return total


def check_valid(check_key_value):
    date_pattern = re.compile("^\d{4}$")
    byr_pattern = re.compile("^19[2-9]\d|^2001|^2002$")
    iyr_pattern = re.compile("^20[1]\d|^2020$")
    eyr_pattern = re.compile("^202\d|^2030$")
    height_pattern = re.compile("^\d+cm|^\d+in$")
    height_type_cm = re.compile("^\d+cm$")
    cm_pattern = re.compile("^1[5-8]\d|^19[0-3]cm$")
    in_pattern = re.compile("^[5-6]\d|^7[0-6]in$")
    hcl_pattern = re.compile("^#[0-9a-f]{6,}$")
    ecl_pattern = re.compile("^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$")
    pid_pattern = re.compile("^[0-9]{9,}$")

    is_valid = True

    for key, value in [entry.split(":") for entry in check_key_value]:
        if key == 'byr' and not (len(date_pattern.findall(value)) > 0 and len(byr_pattern.findall(value)) > 0):
            is_valid = False
            break
        if key == 'iyr' and not (len(date_pattern.findall(value)) > 0 and len(iyr_pattern.findall(value)) > 0):
            is_valid = False
            break
        if key == 'eyr' and not (len(date_pattern.findall(value)) > 0 and len(eyr_pattern.findall(value)) > 0):
            is_valid = False
            break
        if key == 'hgt' and not len(height_pattern.findall(value)) > 0:
            is_valid = False
            break
        if key == 'hgt' and len(height_pattern.findall(value)) > 0:
            if len(height_type_cm.findall(value)) > 0:
                if not len(cm_pattern.findall(value)) > 0:
                    is_valid = False
                    break
            else:
                if not len(in_pattern.findall(value)) > 0:
                    is_valid = False
                    break
        if key == 'hcl' and not len(hcl_pattern.findall(value)) > 0:
            is_valid = False
            break
        if key == 'ecl' and not len(ecl_pattern.findall(value)) > 0:
            is_valid = False
            break
        if key == 'pid' and not len(pid_pattern.findall(value)) > 0:
            is_valid = False
            break

    return is_valid


if __name__ == '__main__':
    input_lines = open('input.txt').readlines()
    entries = [x.strip() for x in input_lines]

    check1 = coalesce_passports(entries)
    answer = check_passports(check1)

    print("answer: ", answer)
