"""
Problem Statement
A positive integer
X
 is said to be a lunlun number if and only if the following condition is satisfied:

In the base ten representation of
X
 (without leading zeros), for every pair of two adjacent digits, the absolute difference of those digits is at most
1
.
For example,
1234
,
1
, and
334
 are lunlun numbers, while none of
31415
,
119
, or
13579
 is.

You are given a positive integer
K
. Find the
K
-th smallest lunlun number.

Constraints
1
≤
K
≤
10
5
All values in input are integers.
Input
Input is given from Standard Input in the following format:

K

Output
Print the answer.

Sample Input 1
Copy
15
Sample Output 1
Copy
23
We will list the
15
 smallest lunlun numbers in ascending order:
1
,
2
,
3
,
4
,
5
,
6
,
7
,
8
,
9
,
10
,
11
,
12
,
21
,
22
,
23
.
Thus, the answer is
23
.

Sample Input 2
Copy
1
Sample Output 2
Copy
1
Sample Input 3
Copy
13
Sample Output 3
Copy
21
Sample Input 4
Copy
100000
Sample Output 4
Copy
3234566667
Note that the answer may not fit into the
32
-bit signed integer type.
"""

# use "Queue" data structure

def update_queue(n, queue):
    out = queue[n]  # result in TLE if use queue.pop(0)...
    mod10 = out % 10
    if mod10 != 0:
        queue.append(10 * out + mod10 - 1)
    queue.append(10 * out + mod10)
    if mod10 != 9:
        queue.append(10 * out + mod10 + 1)

    return out, queue

N = int(input())
Q = [1,2,3,4,5,6,7,8,9]

for i in range(N):
    out, Q = update_queue(i, Q)

print(out)
