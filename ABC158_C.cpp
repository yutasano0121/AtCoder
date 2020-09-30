#include <iostream>
#include <vector>
#include <cmath>

int main(){
  float a, b;
  std::cin >> a >> b;
  std::vector<int> percent8;
  std::vector<int> percent10;

  for (int i = std::ceil(a * 12.5); i < (a + 1) * 12.5; i++){
    percent8.push_back(i);
  }

  for (int i = std::ceil(b * 10); i < (b + 1) * 10 ; i++){
    percent10.push_back(i);
  }

  for (int i = 0; i < percent8.size(); i++){
    if (std::find(percent10.begin(), percent10.end(), percent8[i]) != percent10.end()){
      std::cout << percent8[i];
      return 0;
    }
  }

  std::cout << -1;
  return 0;
}
