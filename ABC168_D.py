N, M = map(int, input().split())

list1 = [-1] * (N + 1)
list2 = [[] for _ in range(N + 1)]
list3 = [-1] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    list2[a].append(b)
    list2[b].append(a)
    s = min(a, b)
    l = max(a, b)
    while list1[s] > 0:
        s = list1[s]
    while list1[l] > 0:
        l = list1[l]
    if s == l:
        continue
    s, l = min(s, l), max(s, l)
    list1[s] += list1[l]
    list1[l] = s

if list1[1] != - N:
    print("No")
else:
    print("Yes")
    list3[1] = 0
    que = list(set(list2[1]))
    count = 1
    while len(que) > 0:
        for i in range(len(que)):
            a = que.pop(0)
            if list3[a] < 0:
                que += list2[a]
                list3[a] = count
        count += 1

    for i in range(2, N + 1):
        for j in list2[i]:
            if list3[i] - 1 == list3[j]:
                print(j)
                continue
