#include <iostream>
#include <string>
#include <vector>

int main(){
  int N, M, s, c;
  std::cin >> N >> M;
  std::string out;
  std::vector<int> called(N, 0);


  for (int i = 0; i < N; i++) out.push_back('0');

  for (int i = 0; i < M; i++){
    std::cin >> s >> c;
    s -= 1;
    if (called[s] == 0){
      called[s] = 1;
      out[s] = c + '0';
    }
    else if (out[s] != c + '0'){
      std::cout << -1;
      return 0;
    }
  }

  if (out[0] == '0'){
    if (called[0] == 1){
      if (N == 1){
        std::cout << 0;
        return 0;
      }
      else{
        std::cout << -1;
        return 0;
      }
    }
    else if (N > 1) out[0] = '1';
  }

  std::cout << out;

  return 0;
}
