import sys
a, b = [int(elem) for elem in sys.stdin.readline().split()]
count = 0

while b >= a:
    a *= 3
    b *= 2
    count += 1

print(count)
