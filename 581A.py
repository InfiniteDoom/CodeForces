import sys
a = sys.stdin.readline().rstrip()
a = a.split()
b = int(a[1])
a = int(a[0])
diff = 0
same = 0

if a < b :
    temp = a
    a = b
    b = temp
a -= b
a /= 2
a = int(a)
diff = b
same = a

print(diff,same)



