# Max sub arrays sum
#
# Note
# Total no of subarrays N(N+1)/2
# Time Complexity O(N)3

arr = [-7, 4, 3, -2, -8, 6, -4, 2]

ans = float('-inf')
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        sum_ = sum(arr[i:j])
        if sum_ > ans:
            ans = sum_
print(ans)

ans = float('-inf')
for i in range(0, len(arr)):
    sum_ = 0
    for j in range(i, len(arr)):
        sum_ += arr[j]
        ans = max(sum_, ans)
print(ans)
