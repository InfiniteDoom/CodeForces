import sys
icount = 0
for i in range(1,6):
    l = sys.stdin.readline().split()
    if '1' in l:
        icount = i
        jcount = l.index('1')
jcount += 1
minMoves = (abs(jcount-3)+abs(icount-3))
print(minMoves)



