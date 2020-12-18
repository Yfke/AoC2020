
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
            a1 = addressSpace(addr, mask)
            for n in allIntegers(a1):
                memory[n] = num
    print(len(memory))
    print(sum(memory.values()))


def allIntegers(s):
    i = s.find('X')
    if i == -1:
        return [int(s, 2)]
    ls1 = list(s)
    ls1[i] = '0'
    ls2 = list(s)
    ls2[i] = '1'
    return allIntegers("".join(ls1)) + allIntegers("".join(ls2))



def addressSpace(n, mask):
    s = list(toBinStr(n))
    for i in range(len(mask)):
        if mask[i] == 'X' or mask[i] == '1':
            s[i] = mask[i]
    return "".join(s)


def dimension(s):
    exp = s.count('X')
    return 2**exp


def overlap(s1, s2):
    result = True
    for i in range(len(s1)):
        if s1[i] == "0" and s2[i] == "1":
            result = False
        if s1[i] == "1" and s2[i] == "0":
            result = False
    if result:
        print("overlap!")


def toBinStr(n):
    s = "{0:b}".format(n)
    return s.zfill(36)


if __name__ == "__main__":
    main()
