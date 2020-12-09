
def main():
    with open("input.txt", "r") as file:
        input = [parse(line) for line in file.read().split("\n\n")]
    valid = 0
    for pas in input:
        if 'byr' not in pas:
            continue
        if 'iyr' not in pas:
            continue
        if 'eyr' not in pas:
            continue
        if 'hgt' not in pas:
            continue
        if 'hcl' not in pas:
            continue
        if 'ecl' not in pas:
            continue
        if 'pid' not in pas:
            continue
        valid += 1
    print(valid)


def parse(line):
    items = line.split()
    dict = {}
    for item in items:
        keyval = item.split(":")
        dict[keyval[0]] = keyval[1]
    return dict


if __name__ == "__main__":
    main()
