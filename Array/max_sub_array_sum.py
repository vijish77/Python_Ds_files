#Max sub arrays sum
#
# Note
# Total no of subarrays N(N+1)/2
# Time Complexity O(N)3

arr = [-7, 4, 3, -2, -8, 6, -4, 2]

res = float('-inf')
for i in range(0,len(arr)):
    for j in range(i+1, len(arr)):
        sum_= sum(arr[i:j])
        if sum_ > res:
            res = sum_
print(res)


