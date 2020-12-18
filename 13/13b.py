from numpy import prod


def main():
    with open("input.txt", "r") as file:
        input = file.read().splitlines()
    mytime = int(input[0])
    ids = [int(s) if s != "x" else 0 for s in input[1].split(",")]
    eqs = [((ids[i] - i) % ids[i], ids[i]) for i in range(len(ids)) if ids[i] != 0]
    print(eqs)

    print(chineseRemainder(eqs))


def chineseRemainder(eqs):
    a1, n1 = eqs[0]
    a2, n2 = eqs[1]
    _, m1, m2 = extendedEuclidean(n1, n2)
    a12 = (a1*m2*n2 + a2*m1*n1) % (n1*n2)
    if len(eqs) == 2:
        return a12
    newEqs = [(a12, n1*n2)] + eqs[2:]
    return chineseRemainder(newEqs)


# find x and y such that xa + yb = gcd(a,b)
# for us, a and b are always coprime
def extendedEuclidean(a, b):
    s, old_s = 0, 1
    r, old_r = b, a

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q*r
        old_s, s = s, old_s - q*s

    t = 0 if b == 0 else (old_r - old_s*a) // b
    return 1, old_s, t


def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x, y = gcdExtended(b % a, a)
    return gcd, y - (b//a) * x, x

if __name__ == "__main__":
    main()
