"""
D - Wizard in Maze  /
実行時間制限: 2 sec / メモリ制限: 1024 MB

Score :
400
 points

Problem Statement
A maze is composed of a grid of
H
×
W
 squares -
H
 vertical,
W
 horizontal.

The square at the
i
-th row from the top and the
j
-th column from the left -
(
i
,
j
)
 - is a wall if
S
i
j
 is # and a road if
S
i
j
 is ..

There is a magician in
(
C
h
,
C
w
)
. He can do the following two kinds of moves:

Move A: Walk to a road square that is vertically or horizontally adjacent to the square he is currently in.
Move B: Use magic to warp himself to a road square in the
5
×
5
 area centered at the square he is currently in.
In either case, he cannot go out of the maze.

At least how many times does he need to use the magic to reach
(
D
h
,
D
w
)
?

Constraints
1
≤
H
,
W
≤
10
3
1
≤
C
h
,
D
h
≤
H
1
≤
C
w
,
D
w
≤
W
S
i
j
 is # or ..
S
C
h
C
w
 and
S
D
h
D
w
 are ..
(
C
h
,
C
w
)
≠
(
D
h
,
D
w
)
Input
Input is given from Standard Input in the following format:

H

W

C
h

C
w

D
h

D
w

S
11
…
S
1
W

⋮

S
H
1
…
S
H
W

Output
Print the minimum number of times the magician needs to use the magic. If he cannot reach
(
D
h
,
D
w
)
, print -1 instead.

Sample Input 1
Copy
4 4
1 1
4 4
..#.
..#.
.#..
.#..
Sample Output 1
Copy
1
For example, by walking to
(
2
,
2
)
 and then using the magic to travel to
(
4
,
4
)
, just one use of magic is enough.

Note that he cannot walk diagonally.

Sample Input 2
Copy
4 4
1 4
4 1
.##.
####
####
.##.
Sample Output 2
Copy
-1
He cannot move from there.

Sample Input 3
Copy
4 4
2 2
3 3
....
....
....
....
Sample Output 3
Copy
0
No use of magic is needed.

Sample Input 4
Copy
4 5
1 2
2 5
#.###
####.
#..##
#..##
Sample Output 4
Copy
2
"""

def walk(h, w, maze, que, step):
    search_area = ((h, w - 1), (h, w + 1), (h - 1, w), (h + 1, w))
    for i in range(4):
        search_cell = search_area[i]
        condition1 = search_cell[0] in range(H)
        condition2 = search_cell[1] in range(W)
        if condition1 and condition2:
            if maze[search_cell[0]][search_cell[1]] == '.':
                que.append(search_cell)
                maze[search_cell[0]][search_cell[1]] = step


def warp(h, w, maze, que, step):
    for i in range(-2, 3):
        for j in range(-2, 3):
            search_cell = (h + i, w + j)
            condition1 = search_cell[0] in range(H)
            condition2 = search_cell[1] in range(W)
            if condition1 and condition2:
                if maze[search_cell[0]][search_cell[1]] == '.':
                    que.append(search_cell)
                    maze[search_cell[0]][search_cell[1]] = step


H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())
maze = [list(input()) for _ in range(H)]

ques = [[(Ch - 1, Cw - 1)]]  # list of list of tuples
step = 0

i = 0
while True:
    try:
        walk(h=ques[step][i][0], w=ques[step][i][1],
             maze=maze, que=ques[step], step=step)
        i += 1
    except:
        step += 1
        ques.append([])
        break

while True:
    for cell in ques[step - 1]:
        warp(h=cell[0], w=cell[1], maze=maze, que=ques[step], step=step)
    if ques[step] == []:
        break
    else:
        i = 0
        while True:
            try:
                walk(h=ques[step][i][0], w=ques[step][i][1],
                     maze=maze, que=ques[step], step=step)
                i += 1
            except:
                step += 1
                ques.append([])
                break

if type(maze[Dh - 1][Dw - 1]) == int:
    print(maze[Dh - 1][Dw - 1])
else:
    print(-1)
