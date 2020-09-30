S = input()
Q = int(input())
rev = 1

head = []
tail = []

for i in range(Q):
  line = input()
  if line == '1':
    rev *= -1
  else:
    line = line.split()
    F = int(line[1])
    C = line[2]
    if rev * F in [1, -2]:
      head.append(C)
    else:
      tail.append(C)

head = head[::-1]
S = ''.join(head + [S] + tail)

if rev == -1:
  S = S[::-1]

print(S)
