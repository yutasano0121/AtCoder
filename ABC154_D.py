N, K = map(int, input().split())
nums = list(map(int, input().split()))

sum_num = sum(nums[:K])
max_num = sum_num

for i in range(1, N - K + 1):
  sum_num = sum_num - nums[i - 1] + nums[i + K - 1]
  if sum_num > max_num:
    max_num = sum_num

print((max_num + K) / 2)
