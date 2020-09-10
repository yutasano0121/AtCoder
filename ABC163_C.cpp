/*
Problem Statement
A company has
N
 members, who are assigned ID numbers
1
,
.
.
.
,
N
.

Every member, except the member numbered
1
, has exactly one immediate boss with a smaller ID number.

When a person
X
 is the immediate boss of a person
Y
, the person
Y
 is said to be an immediate subordinate of the person
X
.

You are given the information that the immediate boss of the member numbered
i
 is the member numbered
A
i
. For each member, find how many immediate subordinates it has.

Constraints
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
<
i
Input
Input is given from Standard Input in the following format:

N

A
2

.
.
.

A
N

Output
For each of the members numbered
1
,
2
,
.
.
.
,
N
, print the number of immediate subordinates it has, in its own line.

Sample Input 1
Copy
5
1 1 2 2
Sample Output 1
Copy
2
2
0
0
0
The member numbered
1
 has two immediate subordinates: the members numbered
2
 and
3
.

The member numbered
2
 has two immediate subordinates: the members numbered
4
 and
5
.

The members numbered
3
,
4
, and
5
 do not have immediate subordinates.

Sample Input 2
Copy
10
1 1 1 1 1 1 1 1 1
Sample Output 2
Copy
9
0
0
0
0
0
0
0
0
0
Sample Input 3
Copy
7
1 2 3 4 5 6
Sample Output 3
Copy
1
1
1
1
1
1
0
*/

#include <vector>
#include <iostream>

int main(){
  int N;
  std::cin >> N;

  std::vector<int> ppl(N, 0);

  int num;
  while (std::cin >> num) ppl[num - 1]++;

  for (int i = 0; i < N; i++) std::cout << ppl[i] << std::endl;

  return 0;
}
