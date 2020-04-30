import sys
n = int(sys.stdin.readline())
games = sys.stdin.readline()
games  = games.rstrip()
total = len(games)
games = games.replace('A','')
D = len(games)
winner = ""
if total - D > D:
    winner = "Anton"
elif total - D < D:
    winner = "Danik"
else:
    winner = "Friendship"
print(winner)
