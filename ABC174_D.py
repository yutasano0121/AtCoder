"""
Problem Statement
An altar enshrines
N
 stones arranged in a row from left to right. The color of the
i
-th stone from the left
(
1
≤
i
≤
N
)
 is given to you as a character
c
i
; R stands for red and W stands for white.

You can do the following two kinds of operations any number of times in any order:

Choose two stones (not necessarily adjacent) and swap them.
Choose one stone and change its color (from red to white and vice versa).
According to a fortune-teller, a white stone placed to the immediate left of a red stone will bring a disaster. At least how many operations are needed to reach a situation without such a white stone?

Constraints
2
≤
N
≤
200000
c
i
 is R or W.
Input
Input is given from Standard Input in the following format:

N

c
1
c
2
.
.
.
c
N

Output
Print an integer representing the minimum number of operations needed.

Sample Input 1
Copy
4
WWRR
Sample Output 1
Copy
2
For example, the two operations below will achieve the objective.

Swap the
1
-st and
3
-rd stones from the left, resulting in RWWR.
Change the color of the
4
-th stone from the left, resulting in RWWW.
Sample Input 2
Copy
2
RR
Sample Output 2
Copy
0
It can be the case that no operation is needed.

Sample Input 3
Copy
8
WRWWRWRR
Sample Output 3
Copy
3
"""

N = int(input())
Stones = list(input())

count_red = 0
count_white = 0

for i in range(N):
    if Stones[i] == "R":
        count_red += 1

for i in range(count_red):
    if Stones[i] == "W":
        count_white += 1

print(count_white)
