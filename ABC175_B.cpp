/*
Problem Statement
We have sticks numbered
1
,
⋯
,
N
. The length of Stick
i

(
1
≤
i
≤
N
)
 is
L
i
.

In how many ways can we choose three of the sticks with different lengths that can form a triangle?

That is, find the number of triples of integers
(
i
,
j
,
k
)

(
1
≤
i
<
j
<
k
≤
N
)
 that satisfy both of the following conditions:

L
i
,
L
j
, and
L
k
 are all different.
There exists a triangle whose sides have lengths
L
i
,
L
j
, and
L
k
.
Constraints
1
≤
N
≤
100
1
≤
L
i
≤
10
9
All values in input are integers.
Input
Input is given from Standard Input in the following format:

N

L
1

L
2

⋯

L
N

Output
Print the number of ways to choose three of the sticks with different lengths that can form a triangle.

Sample Input 1
Copy
5
4 4 9 7 5
Sample Output 1
Copy
5
The following five triples
(
i
,
j
,
k
)
 satisfy the conditions:
(
1
,
3
,
4
)
,
(
1
,
4
,
5
)
,
(
2
,
3
,
4
)
,
(
2
,
4
,
5
)
, and
(
3
,
4
,
5
)
.

Sample Input 2
Copy
6
4 5 4 3 3 5
Sample Output 2
Copy
8
We have two sticks for each of the lengths
3
,
4
, and
5
. To satisfy the first condition, we have to choose one from each length.

There is a triangle whose sides have lengths
3
,
4
, and
5
, so we have
2
3
=
8
 triples
(
i
,
j
,
k
)
 that satisfy the conditions.

Sample Input 3
Copy
10
9 4 6 1 9 6 10 6 6 8
Sample Output 3
Copy
39
Sample Input 4
Copy
2
1 1
Sample Output 4
Copy
0
No triple
(
i
,
j
,
k
)
 satisfies
1
≤
i
<
j
<
k
≤
N
, so we should print
0
.

*/

using namespace std;
#include <iostream>
#include <algorithm>
#include <vector>

int triangle(int N, vector<int> L){
    if (N < 3) return 0;

    int first, second, third, count = 0;
    for (int i = 0; i < L.size() - 2; i++){
        for (int j = i + 1; j < L.size() - 1; j++){
            for (int k = j + 1; k < L.size(); k++){
                first = L[i];
                second = L[j];
                third = L[k];
                if ((first != second && first != third) && second!= third){
                    if (first + second > third) count += 1;
                }
            }
        }
    }
    return count;
}


int main(){
    int N;
    cin >> N;
    int input;
    vector<int> L;
    while (cin >> input) {
      L.push_back(input);
    }
    sort(L.begin(), L.end());
    cout << triangle(N, L);

    return 0;
}
