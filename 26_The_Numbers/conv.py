nums = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]

nl = len(nums)
for i in range(nl):
  print(chr(nums[i] + ord('a') - 1), end="")