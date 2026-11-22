def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] > target:
            right=  mid - 1
        elif arr[mid] < target:
            left = mid +1
        else:
            return True
    return False

def intersection_array(nums1, nums2):
    nums1.sort()
    nums2.sort()
    result = []
    for num in nums1:
        if num not in result:
            if binary_search(nums2, num):
                result.append(num)
    return result
nums1 = [1, 2, 2, 1]
nums2 =[2,2]
print(intersection_array(nums1,nums2))
