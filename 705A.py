import sys
n = int(sys.stdin.readline())
times = 0

if n == 1:
    text = "I hate it"
else:
    times = int(n / 2)
    if n % 2 == 1:
        text = times*"I hate that I love that " +"I hate it"
    else:
        text = (times-1)*"I hate that I love that " + "I hate that I love it"
print(text)


