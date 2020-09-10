"""
Problem Statement
Give a pair of integers
(
A
,
B
)
 such that
A
5
−
B
5
=
X
. It is guaranteed that there exists such a pair for the given integer
X
.

Constraints
1
≤
X
≤
10
9
X
 is an integer.
There exists a pair of integers
(
A
,
B
)
 satisfying the condition in Problem Statement.
Input
Input is given from Standard Input in the following format:

X

Output
Print
A
 and
B
, with space in between. If there are multiple pairs of integers
(
A
,
B
)
 satisfying the condition, you may print any of them.

A

B

Sample Input 1
Copy
33
Sample Output 1
Copy
2 -1
For
A
=
2
 and
B
=
−
1
,
A
5
−
B
5
=
33
.

Sample Input 2
Copy
1
Sample Output 2
Copy
0 -1
"""

X = int(input())

quint = [0] * 1001

for i in range(1, 1001):
    quint[i] = i ** 5

for i in range(0, 1001):
    a = X - quint[i]
    b = X + quint[i]
    try:
        c = quint.index(a)
        print("{} {}".format(c, -i))
        break
    except:
        try:
            c = quint.index(b)
            print("{} {}".format(c, i))
            break
        except:
            continue
