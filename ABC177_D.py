"""
Problem Statement
There are
N
 persons called Person
1
 through Person
N
.

You are given
M
 facts that "Person
A
i
 and Person
B
i
 are friends." The same fact may be given multiple times.

If
X
 and
Y
 are friends, and
Y
 and
Z
 are friends, then
X
 and
Z
 are also friends. There is no friendship that cannot be derived from the
M
 given facts.

Takahashi the evil wants to divide the
N
 persons into some number of groups so that every person has no friend in his/her group.

At least how many groups does he need to make?

Constraints
2
≤
N
≤
2
×
10
5
0
≤
M
≤
2
×
10
5
1
≤
A
i
,
B
i
≤
N
A
i
≠
B
i
Input
Input is given from Standard Input in the following format:

N

M

A
1

B
1

⋮

A
M

B
M

Output
Print the answer.

Sample Input 1
Copy
5 3
1 2
3 4
5 1
Sample Output 1
Copy
3
Dividing them into three groups such as
{
1
,
3
}
,
{
2
,
4
}
, and
{
5
}
 achieves the goal.

Sample Input 2
Copy
4 10
1 2
2 1
1 2
2 1
1 2
1 3
1 4
2 3
2 4
3 4
Sample Output 2
Copy
4
Sample Input 3
Copy
10 4
3 1
4 1
5 9
2 6
Sample Output 3
Copy
3
"""

# solve using union find

N, M = map(int, input().split())  # M pieces of information for N people

# if a parent, -1 * number of members
# else index of its parent
UF = [-1] * N


def root(x):
    if UF[x] < 0:
        return x
    else:
        return root(UF[x])

for _ in range(M):
    a, b = map(int, input().split())
    a = root(a - 1)
    b = root(b - 1)

    if a != b:
        UF[a] += UF[b]
        UF[b] = a

print(-1 * min(UF))
