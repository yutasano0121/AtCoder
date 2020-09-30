/*
Problem Statement
Given any integer
x
, Aoki can do the operation below.

Operation: Replace
x
 with the absolute difference of
x
 and
K
.

You are given the initial value of an integer
N
. Find the minimum possible value taken by
N
 after Aoki does the operation zero or more times.

Constraints
0
≤
N
≤
10
18
1
≤
K
≤
10
18
All values in input are integers.
Input
Input is given from Standard Input in the following format:

N

K

Output
Print the minimum possible value taken by
N
 after Aoki does the operation zero or more times.

Sample Input 1
Copy
7 4
Sample Output 1
Copy
1
Initially,
N
=
7
.

After one operation,
N
 becomes
|
7
−
4
|
=
3
.

After two operations,
N
 becomes
|
3
−
4
|
=
1
, which is the minimum value taken by
N
.

Sample Input 2
Copy
2 6
Sample Output 2
Copy
2
N
=
2
 after zero operations is the minimum.

Sample Input 3
Copy
1000000000000000000 1
Sample Output 3
Copy
0
*/

#include <iostream>

int main(){
  unsigned long long N, K;
  std::cin >> N >> K;

  if (N >= K) N = N % K;

  if (N <= K - N) std::cout << N;
  else std::cout << K - N;

  return 0;
}
