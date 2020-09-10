"""
Problem Statement
Given is a number sequence
A
 of length
N
.

Find the number of integers
i

(
1
≤
i
≤
N
)
 with the following property:

For every integer
j

(
1
≤
j
≤
N
)
 such that
i
≠
j
,
A
j
 does not divide
A
i
.
Constraints
All values in input are integers.
1
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
6
Input
Input is given from Standard Input in the following format:

N

A
1

A
2

⋯

A
N

Output
Print the answer.

Sample Input 1
Copy
5
24 11 8 3 16
Sample Output 1
Copy
3
The integers with the property are
2
,
3
, and
4
.

Sample Input 2
Copy
4
5 5 5 5
Sample Output 2
Copy
0
Note that there can be multiple equal numbers.

Sample Input 3
Copy
10
33 18 45 28 8 19 89 86 2 4
Sample Output 3
Copy
5
"""

# sieve of Eratosthenes
# there should be a better way...
N = int(input())
As = sorted(list(map(int, input().split())))

sieve = [True] * 1000001

prev = 0

for i in range(N):
    if As[i] == prev:
        sieve[As[i]] = False
        continue
    else:
        prev = As[i]
        try:
            for j in range(2, 1000000 // prev + 1):
                sieve[prev * j] = False
        except:
            continue

count = 0
As = list(set(As))
for i in range(len(As)):
    if sieve[As[i]] is True:
        count += 1

print(count)
