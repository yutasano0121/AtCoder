#include <iostream>

int main(){
  int N, k, min = 200000, answer = 0;
  std::cin >> N;

  while (std::cin >> k){
    if (k <= min){
      answer += 1;
      min = k;
    }
  }

  std::cout << answer;

  return 0;
}
