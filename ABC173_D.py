"""
Problem Statement
Quickly after finishing the tutorial of the online game ATChat, you have decided to visit a particular place with
N
−
1
 players who happen to be there. These
N
 players, including you, are numbered
1
 through
N
, and the friendliness of Player
i
 is
A
i
.

The
N
 players will arrive at the place one by one in some order. To make sure nobody gets lost, you have set the following rule: players who have already arrived there should form a circle, and a player who has just arrived there should cut into the circle somewhere.

When each player, except the first one to arrive, arrives at the place, the player gets comfort equal to the smaller of the friendliness of the clockwise adjacent player and that of the counter-clockwise adjacent player. The first player to arrive there gets the comfort of
0
.

What is the maximum total comfort the
N
 players can get by optimally choosing the order of arrivals and the positions in the circle to cut into?

Constraints
All values in input are integers.
2
≤
N
≤
2
×
10
5
1
≤
A
i
≤
10
9
Input
Input is given from Standard Input in the following format:

N

A
1

A
2

…

A
N

Output
Print the maximum total comfort the
N
 players can get.

Sample Input 1
Copy
4
2 2 1 3
Sample Output 1
Copy
7
By arriving at the place in the order Player
4
,
2
,
1
,
3
, and cutting into the circle as shown in the figure, they can get the total comfort of
7
.

Figure

They cannot get the total comfort greater than
7
, so the answer is
7
.

Sample Input 2
Copy
7
1 1 1 1 1 1 1
Sample Output 2
Copy
6
"""

N = int(input())

As = sorted(map(int, input().split()), reverse=True)

score = As[0]
counter = 0
index = 1

for i in range(2, N):
  score += As[index]
  if counter == 0:
    counter += 1
  else:
    counter -= 1
    index += 1

print(score)
