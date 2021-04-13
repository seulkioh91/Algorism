# 단순삽입법=버블정렬(bubblesort)
def bsort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


arr= bsort([5,3,4,1,2])
print(arr)
