N = int(input())

d = {}

for i in range(N):
  key = input()
  try:
    d[key] += 1
  except KeyError:
    d[key] = 1

d = sorted(d.items(), key=lambda x: x[1], reverse=True)

ans = []
max = 0
for i in d:
  if i[1] >= max:
    ans.append(i[0])
    max = i[1]
  else:
    break

for i in sorted(ans):
  print(i)
