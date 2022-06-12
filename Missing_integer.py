#This code finds the smallest positive integer not in a given list. For example:
# [1, 2, 3] returns 4
# [1, 2, 3, 4, 6] returns 5
# [-3, -1] returns 1

def missing_integer(a):
  pos = []
  for x in a:
    if x+1 <= 0:
      pos.append(1)
    elif x+1 in a:
      pass
    elif x+1 not in a:
      pos.append(x+1)
  return min(pos)

print(missing_integer([-1, -2]))
