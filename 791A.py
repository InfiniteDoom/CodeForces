import sys
a, b = [int(elem) for elem in sys.stdin.readline().split()]
a = int(a)
b = int(b)
count = 0

while b >= a:
    a *= 3
    b *= 2
    count += 1

print(count)
