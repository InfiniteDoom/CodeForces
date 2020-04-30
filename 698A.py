days = int(input())
activities = input().split()
count = 0
current = 0
restDay = 0
aOrB = 0

for x in range(0, len(activities)):    
  if count == 0:
      count += 1
      current = activities[x]
  elif activities[x] == 0:
      restDay += 1
      current = activities[x]
  elif activities[x] == 1:
      if current == 1:
          restDay += 1
      elif current == 3:
          if aOrB == 1:
              restDay += 1
      current = activities[x]
  elif activities[x] == 2:
      if current == 2:
          restDay += 1
      elif current == 3:
          if aOrB == 0:
              restDay += 1
      current = activities[x]
  elif activities[x] == 3:
      if current == 1:
          current = 2
          aOrB = 0
      elif current == 2:
          current = 1
          aOrB = 1
      elif current == 3:
          if current != 0:
              if aOrB == 0:
                  current = 1
              else:
                  current = 2
          else:
              if activities[x+1] == 1:
                  current = 2
              else:
                  current = 1


print(restDay)
     
