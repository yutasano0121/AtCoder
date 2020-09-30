import copy
H, W = map(int, input().split())
maze = [input() for _ in range(H)]
maze_ = [[-1 for _ in range(W)] for __ in range(H)]

max_steps = 0

for i in range(H):
  for j in range(W):
    if maze[i][j] == '#':
      continue
    else:
      maze2 = copy.deepcopy(maze_)
      que = [(i, j)]
      steps = [0]
      loc = 0
      while True:
        try:
          current_loc = que[loc]
          i_, j_ = current_loc[0], current_loc[1]
          maze2[i_][j_] = steps[loc]
          nexts = [(i_, j_ + 1), (i_, j_ - 1), (i_ + 1, j_), (i_ - 1, j_)]
          for n in nexts:
            if ((((n[0] < H and n[0] >= 0) and n[1] < W) and n[1] >= 0) and maze[n[0]][n[1]] == '.') and maze2[n[0]][n[1]] == -1:
              que.append(n)
              steps.append(maze2[i_][j_] + 1)
          loc += 1
        except:
          max_steps = max(max_steps, steps[-1])
          break
      if max_steps == H + W - 2:
        break

print(max_steps)
