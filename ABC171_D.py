"""
Input is given from Standard Input in the following format:

N

A
1

A
2

⋯

A
N

Q

B
1

C
1

B
2

C
2

⋮

B
Q

C
Q

Output
Print
Q
 integers
S
i
 to Standard Output in the following format:

S
1

S
2

⋮

S
Q

Note that
S
i
 may not fit into a
32
-bit integer.

Sample Input 1
Copy
4
1 2 3 4
3
1 2
3 4
2 4
Sample Output 1
Copy
11
12
16
Initially, the sequence
A
 is
1
,
2
,
3
,
4
.

After each operation, it becomes the following:

2
,
2
,
3
,
4
2
,
2
,
4
,
4
4
,
4
,
4
,
4
Sample Input 2
Copy
4
1 1 1 1
3
1 2
2 1
3 5
Sample Output 2
Copy
8
4
4
Note that the sequence
A
 may not contain an element whose value is
B
i
.

Sample Input 3
Copy
2
1 2
3
1 100
2 100
100 1000
Sample Output 3
Copy
102
200
2000
"""

N = int(input())
As = list(map(int, input().split()))
Q = int(input())

sumAs = 0
dictAs = [0] * 100000
for i in range(len(As)):
  sumAs += As[i]
  dictAs[As[i] - 1] += 1


for _ in range(Q):
  b, c = map(int, input().split())
  sumAs += dictAs[b - 1] * (c - b)
  dictAs[c - 1] += dictAs[b - 1]
  dictAs[b - 1] = 0
  print(sumAs)
