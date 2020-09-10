N, K = map(int, input().split())
warp = list(map(int, input().split()))
warp = [i - 1 for i in warp]

visit = [0]

current_loc = 0
while warp[current_loc] != -1:
    visit.append(warp[current_loc])
    warp[current_loc] = -1
    current_loc = visit[-1]

res = visit.index(visit[-1])
cycle = visit[res + 1:]
if K <= res:
    print(visit[K] + 1)
else:
    answer = cycle[(K - res - 1) % (len(visit) - 1 - res)] + 1
    print(answer)
