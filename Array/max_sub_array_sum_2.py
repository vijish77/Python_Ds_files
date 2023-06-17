# Max sub arrays sum
# Kadanes Algorithm (mqaximum sub array in linear comnplexity)
# Note
# Total no of subarrays N(N+1)/2
# Time Complexity O(N)

sum_, ans = 0, float('-inf')
#arr = [5, 6, 7, -3, 2, -10, -12, 8, 12, 21, -4, 7]
arr = [-20, -10, -6, -15, -2, -30]
for i in range(0, len(arr)):
    sum_ += arr[i]
    ans = max(sum_, ans)
    if sum_ < 0:
        sum_ = 0
print(ans)
