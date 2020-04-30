import sys
n, m = sys.stdin.readline().split()
n = int(n)
m = int(m)
aDesc = [int(elem) for elem in sys.stdin.readline().split()]
i = 0
j = 0
minEarnings = 0
maxEarnings = 0

if sum(aDesc) == n:
    for x in range(0, n):
        if aDesc[i] == 0:
            i += 1
        maxEarnings += aDesc[i]
        aDesc[i] -= 1
    print(maxEarnings, maxEarnings)

else:
    aDesc.sort()
    aAsc = list(aDesc)
    aDesc.sort(reverse = True)

    # max earnings
    for x in range(0, n):
        if i == m - 1:
            if aDesc[i] == 0:
                for x in range (0,m):
                    if aDesc[x] != 0:
                        i = x
        elif aDesc[i] < aDesc[i+1]:
            i += 1
        maxEarnings += aDesc[i]
        aDesc[i] -= 1
        aDesc.sort(reverse = True)

    # min earnings
    for y in range(0, n):
        if aAsc[j] == 0:
            j += 1
        minEarnings += aAsc[j]
        aAsc[j] -= 1

    print(maxEarnings, minEarnings)
