"""
Problem Statement
1000000000000001
 dogs suddenly appeared under the roof of Roger's house, all of which he decided to keep. The dogs had been numbered
1
 through
1000000000000001
, but he gave them new names, as follows:

the dogs numbered
1
,
2
,
⋯
,
26
 were respectively given the names a, b, ..., z;
the dogs numbered
27
,
28
,
29
,
⋯
,
701
,
702
 were respectively given the names aa, ab, ac, ..., zy, zz;
the dogs numbered
703
,
704
,
705
,
⋯
,
18277
,
18278
 were respectively given the names aaa, aab, aac, ..., zzy, zzz;
the dogs numbered
18279
,
18280
,
18281
,
⋯
,
475253
,
475254
 were respectively given the names aaaa, aaab, aaac, ..., zzzy, zzzz;
the dogs numbered
475255
,
475256
,
⋯
 were respectively given the names aaaaa, aaaab, ...;
and so on.
To sum it up, the dogs numbered
1
,
2
,
⋯
 were respectively given the following names:

a, b, ..., z, aa, ab, ..., az, ba, bb, ..., bz, ..., za, zb, ..., zz, aaa, aab, ..., aaz, aba, abb, ..., abz, ..., zzz, aaaa, ...

Now, Roger asks you:

"What is the name for the dog numbered
N
?"

Constraints
N
 is an integer.
1
≤
N
≤
1000000000000001
Input
Input is given from Standard Input in the following format:

N

Output
Print the answer to Roger's question as a string consisting of lowercase English letters.

Sample Input 1
Copy
2
Sample Output 1
Copy
b
Sample Input 2
Copy
27
Sample Output 2
Copy
aa
Sample Input 3
Copy
123456789
Sample Output 3
Copy
jjddja

"""

N = int(input())

alp = "abcdefghijklmnopqrstuvwxyz"
answer = ""

while N != 0:
  N -= 1
  index = N % 26
  answer += alp[index]
  N = N // 26

print(answer[::-1])
