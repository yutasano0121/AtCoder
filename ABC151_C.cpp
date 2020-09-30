#include <iostream>
#include <string>
#include <vector>

int main(){
  int N, M;
  std::cin >> N >> M;

  int q = 0, ac = 0, wa = 0;
  std::vector<int> answered(N, 0);
  int p;
  std::string s;

  for (int i = 0; i < M; i++){
    std::cin >> p >> s;
    if (answered[p] == -1) continue;
    else if (s == "WA") answered[p]++;
    else {
      ac++;
      wa += answered[p];
      answered[p] = -1;
    }
  }

  std::cout << ac << ' ' << wa;

  return 0;
}
