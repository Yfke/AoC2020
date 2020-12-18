
def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    memory = {}
    for line in input:
        if line[0:4] == "mask":
            mask = line[7:]
        else:
            [addr, num] = [int(n) for n in line[4:].split("] = ")]
            memory[addr] = computeNumber(num, mask)
    # print(memory)
    print(sum(memory.values()))


def computeNumber(n, mask):
    s = list(toBinStr(n))
    for i in range(len(mask)):
        if mask[i] == '0' or mask[i] == '1':
            s[i] = mask[i]
    return int("".join(s), 2)



def toBinStr(n):
    s = "{0:b}".format(n)
    return s.zfill(36)


if __name__ == "__main__":
    main()
