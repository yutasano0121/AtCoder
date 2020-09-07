/*
Problem Statement
We have a grid of
H
 rows and
W
 columns of squares. The color of the square at the
i
-th row from the top and the
j
-th column from the left
(
1
≤
i
≤
H
,
1
≤
j
≤
W
)
 is given to you as a character
c
i
,
j
: the square is white if
c
i
,
j
 is ., and black if
c
i
,
j
 is #.

Consider doing the following operation:

Choose some number of rows (possibly zero), and some number of columns (possibly zero). Then, paint red all squares in the chosen rows and all squares in the chosen columns.
You are given a positive integer
K
. How many choices of rows and columns result in exactly
K
 black squares remaining after the operation? Here, we consider two choices different when there is a row or column chosen in only one of those choices.

Constraints
1
≤
H
,
W
≤
6
1
≤
K
≤
H
W
c
i
,
j
 is . or #.
Input
Input is given from Standard Input in the following format:

H

W

K

c
1
,
1
c
1
,
2
.
.
.
c
1
,
W

c
2
,
1
c
2
,
2
.
.
.
c
2
,
W

:

c
H
,
1
c
H
,
2
.
.
.
c
H
,
W

Output
Print an integer representing the number of choices of rows and columns satisfying the condition.

Sample Input 1
Copy
2 3 2
..#
###
Sample Output 1
Copy
5
Five choices below satisfy the condition.

The
1
-st row and
1
-st column
The
1
-st row and
2
-nd column
The
1
-st row and
3
-rd column
The
1
-st and
2
-nd column
The
3
-rd column
Sample Input 2
Copy
2 3 4
..#
###
Sample Output 2
Copy
1
One choice, which is choosing nothing, satisfies the condition.

Sample Input 3
Copy
2 2 3
##
##
Sample Output 3
Copy
0
Sample Input 4
Copy
6 6 8
..##..
.#..#.
#....#
######
#....#
#....#
Sample Output 4
Copy
208
*/

// choice of rows/columns corresponds to bits between 1~H and 1~W

using namespace std;
#include <iostream>
#include <string>
#include <vector>
#include <bitset>

int main(){
  int H, W, K;
  cin >> H >> W >> K;

  vector<string> grid;
  string row;
  for (int i = 0; i < H; i++){
    cin >> row;
    grid.push_back(row);
  }

  int score = 0;
  bool cond1, cond2, cond3;

  for (int h = 0; h < (1 << H); h++){
    for (int w = 0; w < (1 << W); w++){
      int black = 0;
      for (int i = 0; i < H; i++){
        for (int j = 0; j < W; j++){
          cond1 = ((h >> i) & 1) == 1;
          cond2 = ((w >> j) & 1) == 1;
          cond3 = grid[i][j] == '#';

          if ((cond1 && cond2) && cond3) black += 1;
        }
      }
      if (black == K) score += 1;
    }
  }

  cout << score;

  return 0;
}
