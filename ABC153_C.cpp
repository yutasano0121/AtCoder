#include <iostream>
#include <vector>
#include <algorithm>

int main(){
  int N, K;
  std::cin >> N >> K;

  if (K >= N){
    std::cout << 0;
    return 0;
  }

  std::vector<unsigned long> nums;
  unsigned long n;

  while(std::cin >> n) nums.push_back(n);
  std::sort(nums.begin(), nums.end(), std::greater<unsigned long>());

  unsigned long long sum = 0;
  for (int i = K; i < N; i++) sum += nums[i];

  std::cout << sum;

  return 0;
}
