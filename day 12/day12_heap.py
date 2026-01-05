import heapq
nums=[5, 3, 8, 1, 2, 7]
heapq.heapify(nums)
print(nums)
heapq.heappush(nums, 4)
print(nums)

print(heapq.heappop(nums))
print(nums)

