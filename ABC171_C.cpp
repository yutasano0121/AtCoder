// tedious approach...

using namespace std;
#include <iostream>
#include <vector>
#include <string>

int main(){
  long N;
  cin >> N;

  int digit = 0;
  long accum = 0;
  long fact = 1;
  vector<long> accum_list;
  vector<long> fact_list;

  while(accum < N){
    accum_list.push_back(accum);
    fact_list.push_back(fact);
    digit++;
    fact *= 26;
    accum += fact;
  }


  string answer;
  string alphabet = "abcdefghijklmnopqrstuvwxyz";
  int index;

  if (accum == N){
    while (digit > 0){
      answer.push_back('z');
      digit--;
    }
    cout << answer;
    return 0;
  }


  if (digit > 1){
    digit--;
    N -= accum_list[digit];
    index = N / fact_list[digit];
    if (index * fact_list[digit] == N){
      answer.push_back(alphabet[index - 1]);
      while (digit > 0){
        answer.push_back('z');
        digit--;
      }
      cout << answer;
      return 0;
    }
    answer.push_back(alphabet[index]);
    N -= fact_list[digit] * index;
  }
  while (digit > 1){
    digit--;
    index = N / fact_list[digit];
    if (index * fact_list[digit] == N){
      answer.push_back(alphabet[index - 1]);
      while (digit > 0){
        answer.push_back('z');
        digit--;
      }
      cout << answer;
      return 0;
    }
    answer.push_back(alphabet[index]);
    N -= fact_list[digit] * index;
  }
  answer.push_back(alphabet[N - 1]);



  cout << answer;

  return 0;
}
