win_lose = input()
max_streak = 0
win_streak = 0
for char in win_lose:
  if char == 'W':
    win_streak +=1
    if win_streak>max_streak:
      max_streak=win_streak
  else:
    win_streak= 0

print(max_streak)