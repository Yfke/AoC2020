import re


def main():
    with open("input.txt", "r") as file:
        input = [parse(line) for line in file.read().split("\n\n")]
    valid = 0
    for pas in input:
        if not all(k in pas for k in
                   ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
            # there is field missing, the passport is invalid
            continue
        if (numberTest(pas['byr'], 1920, 2002)
           and numberTest(pas['iyr'], 2010, 2020)
           and numberTest(pas['eyr'], 2020, 2030)
           and heightTest(pas['hgt'])
           and hairTest(pas['hcl'])
           and eyeTest(pas['ecl'])
           and idTest(pas['pid'])):
            # all fields are of the correct form
            valid += 1
    print(valid)


def idTest(str):
    return len(str) == 9 and str.isnumeric()


def eyeTest(str):
    return str in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def hairTest(str):
    return re.match(r"#[0-9a-f]{6}", str) is not None


def heightTest(str):
    return (re.match(r"(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in", str)
            is not None)


def numberTest(str, min, max):
    return str.isnumeric() and min <= int(str) <= max


def parse(line):
    # split() without argument splits on spaces and newlines
    items = [item.split(":") for item in line.split()]
    return {kv[0]: kv[1] for kv in items}


if __name__ == "__main__":
    main()
