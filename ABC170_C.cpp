/*
Problem Statement
Given are an integer
X
 and an integer sequence of length
N
:
p
1
,
…
,
p
N
.

Among the integers not contained in the sequence
p
1
,
…
,
p
N
 (not necessarily positive), find the integer nearest to
X
, that is, find the integer whose absolute difference with
X
 is the minimum. If there are multiple such integers, report the smallest such integer.

Constraints
1
≤
X
≤
100
0
≤
N
≤
100
1
≤
p
i
≤
100
p
1
,
…
,
p
N
 are all distinct.
All values in input are integers.
Input
Input is given from Standard Input in the following format:

X

N

p
1

.
.
.

p
N

Output
Print the answer.

Sample Input 1
Copy
6 5
4 7 10 6 5
Sample Output 1
Copy
8
Among the integers not contained in the sequence
4
,
7
,
10
,
6
,
5
, the one nearest to
6
 is
8
.

Sample Input 2
Copy
10 5
4 7 10 6 5
Sample Output 2
Copy
9
Among the integers not contained in the sequence
4
,
7
,
10
,
6
,
5
, the ones nearest to
10
 are
9
 and
11
. We should print the smaller one,
9
.

Sample Input 3
Copy
100 0

Sample Output 3
Copy
100
When
N
=
0
, the second line in the input will be empty. Also, as seen here,
X
 itself can be the answer.
*/

using namespace std;
#include <iostream>
#include <algorithm>
#include <string>

int main(){
  int X, N;
  cin >> X >> N;
  vector<int> Ps;
  int p;
  while (cin >> p) Ps.push_back(p);

  vector<int> candidate;
  candidate.push_back(X);

  int count = 1;
  int sub = 1;
  while (count < N + 1){
    candidate.push_back(X - sub);
    candidate.push_back(X + sub);
    count += 2;
    sub += 1;
  }

  for (int i = 0; i < candidate.size(); i ++){
    if (find(Ps.begin(), Ps.end(), candidate[i]) == Ps.end()){
      cout << candidate[i];
      return 0;
    }
  }
}
