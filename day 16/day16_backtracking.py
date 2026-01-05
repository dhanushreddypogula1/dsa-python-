def backtrack(path,nums):
    if len(path) == len(nums):
        print(path)
        return
    
    for num in nums:
        if num in path:
            continue
        path.append(num)
        backtrack(path,nums)
        path.pop()
backtrack([], [1,2,3])