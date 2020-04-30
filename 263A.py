import sys
icount = 0
l1 = sys.stdin.readline().split()
l2 = sys.stdin.readline().split()
l3 = sys.stdin.readline().split()
l4 = sys.stdin.readline().split()
l5 = sys.stdin.readline().split()

if '1' in l1:
    icount = 1
    jcount = l1.index('1')
elif '1' in l2:
    icount = 2
    jcount = l2.index('1')
elif '1' in l3:
    icount = 3
    jcount = l3.index('1')
elif '1' in l4:
    icount = 4
    jcount = l4.index('1')
elif '1' in l5:
    icount = 5
    jcount = l5.index('1')

jcount += 1
minMoves = (abs(jcount-3)+abs(icount-3))
print(minMoves)



