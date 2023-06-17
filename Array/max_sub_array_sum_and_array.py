# Max sub arrays sum
# Note
# Kadanes Algorithm (mqaximum sub array in linear comnplexity)
# Total no of subarrays N(N+1)/2
# Time Complexity O(N)

sum_, ans = 0, float('-inf')
arr = [5, 6, 7, -3, 2, -10, -12, 8, 12, 21, -4, 7]
#arr = [-20, -10, -6, -15, -2, -30]
l, r = 0, 0
for i in range(0, len(arr)):
    r = r + 1
    sum_ += arr[i]
    ans = max(sum_, ans)
    if sum_ < 0:
        l = r
        sum_ = 0
print(ans)
print(arr[l:r])
