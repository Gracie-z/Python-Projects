"""
Calculate the product of two arbitrary integers precisely using Long multiplication.
"""


def main(x, y):
    """
    main(x,y) receives two integers as arguments and return their product precisely,
    no matter how large each integer is
    """
    L = [one(x, int(i)) for i in str(y)]  # multiply the multiplicand by each digit of the multiplier
    L.reverse()
    for i in range(len(L)):
        L[i] = int(L[i]) * 10 ** i
    L, m = plus(L) #add up all the properly shifted results
    M = []
    for j in range(m):
        M.append(sum(int(L[i][j]) for i in range(len(L))))
    M = carry(M)
    return M


def one(a, b):
    """
 pass in two integers as arguments: one is arbitrary, the other is in 0~9
    """
    a, b = dis(a, b)  # find out which one is the one-digit integer
    L = [int(x) * a for x in str(b)]
    L.insert(0, 0)
    L = carry(L)  # caculate the carry-overs
    return L


def dis(a, b):
    """
  figure out which one is in 0~9
    """
    if len(str(a)) == 1:
        return a, b
    else:
        return b, a


def carry(L):
    """
    This function deals with the carry-over
    """
    for i in range(len(L)):
        while L[-i] >= 10:
            L[-i] -= 10
            L[-i - 1] += 1
    if L[0] == 0:
        L.pop(0)
    L = ''.join(map(str, L))
    return L


def plus(L):
    """
 This function sums the column entries in the matrix L
 add up all the properly shifted results
    """
    m = len(str(L[-1]))
    for i in range(len(L)):
        L[i] = [num for num in str(L[i])]
        while len(L[i]) < m:
            L[i].insert(0, 0)
    return L, m
