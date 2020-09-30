N = int(input())
As = list(map(int, input().split()))
count_dict = {}


def calc_combo(n):
    return int(n * (n - 1) / 2)


for i in range(N):
    try:
        count_dict[As[i]] += 1
    except KeyError:
        count_dict[As[i]] = 1

combo = 0
for key in count_dict:
    combo += calc_combo(count_dict[key])

for i in range(N):
    num_delete = As[i]
    try:
        num_count = count_dict[num_delete]
        out = combo - calc_combo(num_count) + calc_combo(num_count - 1)
        print(out)
    except KeyError:
        print(combo)
