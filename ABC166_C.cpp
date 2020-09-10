/*
Problem Statement
There are
N
 observatories in AtCoder Hill, called Obs.
1
, Obs.
2
,
.
.
.
, Obs.
N
. The elevation of Obs.
i
 is
H
i
. There are also
M
 roads, each connecting two different observatories. Road
j
 connects Obs.
A
j
 and Obs.
B
j
.

Obs.
i
 is said to be good when its elevation is higher than those of all observatories that can be reached from Obs.
i
 using just one road. Note that Obs.
i
 is also good when no observatory can be reached from Obs.
i
 using just one road.

How many good observatories are there?

Constraints
2
≤
N
≤
10
5
1
≤
M
≤
10
5
1
≤
H
i
≤
10
9
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
Multiple roads may connect the same pair of observatories.
All values in input are integers.
Input
Input is given from Standard Input in the following format:

N

M

H
1

H
2

.
.
.

H
N

A
1

B
1

A
2

B
2

:

A
M

B
M

Output
Print the number of good observatories.

Sample Input 1
Copy
4 3
1 2 3 4
1 3
2 3
2 4
Sample Output 1
Copy
2
From Obs.
1
, you can reach Obs.
3
 using just one road. The elevation of Obs.
1
 is not higher than that of Obs.
3
, so Obs.
1
 is not good.

From Obs.
2
, you can reach Obs.
3
 and
4
 using just one road. The elevation of Obs.
2
 is not higher than that of Obs.
3
, so Obs.
2
 is not good.

From Obs.
3
, you can reach Obs.
1
 and
2
 using just one road. The elevation of Obs.
3
 is higher than those of Obs.
1
 and
2
, so Obs.
3
 is good.

From Obs.
4
, you can reach Obs.
2
 using just one road. The elevation of Obs.
4
 is higher than that of Obs.
2
, so Obs.
4
 is good.

Thus, the good observatories are Obs.
3
 and
4
, so there are two good observatories.

Sample Input 2
Copy
6 5
8 6 9 1 2 1
1 3
4 2
4 3
4 6
4 6
Sample Output 2
Copy
3
*/

#include <iostream>
#include <vector>

int main(){
  int N, M, a, b;
  std::cin >> N >> M;

  std::vector<long> Hs(N, 0);

  for (int i = 0; i < N; i++) std::cin >> Hs[i];

  std::vector<int> heighest(N, 1);

  for (int i = 0; i < M; i++){
    std::cin >> a >> b;
    a--;
    b--;
    if (Hs[a] > Hs[b]) heighest[b] = 0;
    else if (Hs[a] < Hs[b]) heighest[a] = 0;
    else {
      heighest[a] = 0;
      heighest[b] = 0;
    }
  }

  int answer = 0;
  for (int i = 0; i < N; i++) answer += heighest[i];

  std::cout << answer;

  return 0;
}
