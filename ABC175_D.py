"""
Problem Statement
Takahashi will play a game using a piece on an array of squares numbered
1
,
2
,
⋯
,
N
. Square
i
 has an integer
C
i
 written on it. Also, he is given a permutation of
1
,
2
,
⋯
,
N
:
P
1
,
P
2
,
⋯
,
P
N
.

Now, he will choose one square and place the piece on that square. Then, he will make the following move some number of times between
1
 and
K
 (inclusive):

In one move, if the piece is now on Square
i

(
1
≤
i
≤
N
)
, move it to Square
P
i
. Here, his score increases by
C
P
i
.
Help him by finding the maximum possible score at the end of the game. (The score is
0
 at the beginning of the game.)

Constraints
2
≤
N
≤
5000
1
≤
K
≤
10
9
1
≤
P
i
≤
N
P
i
≠
i
P
1
,
P
2
,
⋯
,
P
N
 are all different.
−
10
9
≤
C
i
≤
10
9
All values in input are integers.
Input
Input is given from Standard Input in the following format:

N

K

P
1

P
2

⋯

P
N

C
1

C
2

⋯

C
N

Output
Print the maximum possible score at the end of the game.

Sample Input 1
Copy
5 2
2 4 5 1 3
3 4 -10 -8 8
Sample Output 1
Copy
8
When we start at some square of our choice and make at most two moves, we have the following options:

If we start at Square
1
, making one move sends the piece to Square
2
, after which the score is
4
. Making another move sends the piece to Square
4
, after which the score is
4
+
(
−
8
)
=
−
4
.
If we start at Square
2
, making one move sends the piece to Square
4
, after which the score is
−
8
. Making another move sends the piece to Square
1
, after which the score is
−
8
+
3
=
−
5
.
If we start at Square
3
, making one move sends the piece to Square
5
, after which the score is
8
. Making another move sends the piece to Square
3
, after which the score is
8
+
(
−
10
)
=
−
2
.
If we start at Square
4
, making one move sends the piece to Square
1
, after which the score is
3
. Making another move sends the piece to Square
2
, after which the score is
3
+
4
=
7
.
If we start at Square
5
, making one move sends the piece to Square
3
, after which the score is
−
10
. Making another move sends the piece to Square
5
, after which the score is
−
10
+
8
=
−
2
.
The maximum score achieved is
8
.

Sample Input 2
Copy
2 3
2 1
10 -7
Sample Output 2
Copy
13
Sample Input 3
Copy
3 3
3 1 2
-1000 -2000 -3000
Sample Output 3
Copy
-1000
We have to make at least one move.

Sample Input 4
Copy
10 58
9 1 6 7 8 4 3 2 10 5
695279662 988782657 -119067776 382975538 -151885171 -177220596 -169777795 37619092 389386780 980092719
Sample Output 4
Copy
29507023469
The absolute value of the answer may be enormous.
"""


"""
1st solution
Time limit error
"""

N, K = map(int, input().split())
Ps = list(map(int, input().split()))
Cs = list(map(int, input().split()))


def calcScore(C_list, P_list, idx, num_operation):
    score = 0
    scores = []
    for i in range(num_operation):
        idx = P_list[idx] - 1
        score += C_list[idx]
        scores.append(score)
    return max(scores)


max_scores = [calcScore(Cs, Ps, i, K) for i in range(N)]

print(max(max_scores))


"""
2nd solution
Consider the fact that operation results in cycles
"""

N, K = map(int, input().split())
Ps = list(map(int, input().split()))
Ps = [i - 1 for i in Ps]
Cs = list(map(int, input().split()))
max_score = -float("inf")


for i in range(N):
    scores = []
    idx = i  # starting index
    while True:
        idx = Ps[idx]  # point to the next index
        scores.append(Cs[idx])  # fetch a score to add
        if idx == i:  # when the cycle is closed
            break

    len_cycle = len(scores)
    sum_cycle = sum(scores)

    if sum_cycle <= 0:  # when each cycle reduces the total score
        score = 0
        for j in range(min(K, len_cycle)):
            score += scores[j]
            max_score = max(max_score, score)
    else:
        if K // len_cycle > 0:
            num_multiply = K // len_cycle - 1
            score = sum_cycle * num_multiply
            scores = scores * 2
            for j in range(K % len_cycle + len_cycle):
                score += scores[j]
                max_score = max(max_score, score)
        else:
            num_multiply = 0  # len_cycle > K
            score = sum_cycle * num_multiply
            for j in range(K):
                score += scores[j]
                max_score = max(max_score, score)

print(max_score)
