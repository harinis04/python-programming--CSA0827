def num_good_pairs(nums):
   
    num_counts = {}
    good_pairs = 0


    for num in nums:
        if num in num_counts:
            good_pairs += num_counts[num]
            num_counts[num] += 1 
        else:
            num_counts[num] = 1  

    return good_pairs


nums = [1, 2, 3, 1, 1, 3]
result = num_good_pairs(nums)
print("Number of good pairs:", result)
