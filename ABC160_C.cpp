/*
Problem Statement
There is a circular pond with a perimeter of
K
 meters, and
N
 houses around them.

The
i
-th house is built at a distance of
A
i
 meters from the northmost point of the pond, measured clockwise around the pond.

When traveling between these houses, you can only go around the pond.

Find the minimum distance that needs to be traveled when you start at one of the houses and visit all the
N
 houses.

Constraints
2
≤
K
≤
10
6
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
A
1
<
.
.
.
<
A
N
<
K
All values in input are integers.
Input
Input is given from Standard Input in the following format:

K

N

A
1

A
2

.
.
.

A
N

Output
Print the minimum distance that needs to be traveled when you start at one of the houses and visit all the
N
 houses.

Sample Input 1
Copy
20 3
5 10 15
Sample Output 1
Copy
10
If you start at the
1
-st house and go to the
2
-nd and
3
-rd houses in this order, the total distance traveled will be
10
.

Sample Input 2
Copy
20 3
0 5 15
Sample Output 2
Copy
10
If you start at the
2
-nd house and go to the
1
-st and
3
-rd houses in this order, the total distance traveled will be
10
.
*/

#include <iostream>
#include <vector>

int main(){
  int K, N;
  std::cin >> K >> N;

  int A;
  int max_dist = 0;
  std::vector<int> As;

  for (int i = 0; i < N; i++){
    std::cin >> A;
    As.push_back(A);
    if (i != 0){
      if (As[i] - As[i - 1] > max_dist) max_dist = As[i] - As[i - 1];
    }
  }

  if (As[0] + K - As[N - 1] > max_dist) max_dist = As[0] + K - As[N - 1];

  std::cout << K - max_dist;

  return 0;
}
