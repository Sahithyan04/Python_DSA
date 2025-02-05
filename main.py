# def removeElement( nums, val) :

        
#  r = len(nums) - 1  
#  l = 0 
#  j = 0
#  # k = len(nums) - nums.count(val)

#  while l < r:
#     if nums[r] == val :
#         r -= 1

#     elif nums[l] == val:
#         nums[l],nums[r] = nums[r],nums[l]
#         j += 1
#         l += 1
#         r -= 1
#     else:
#         l+=1
    

#  print(nums)
#  id = nums.index(val)
#  return len( nums[:id])
# nums =[3,1,3,3,3]
# val = 3
# print(removeElement(nums,val))


# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1

#     while low <= high:
        
#         mid = (high + low) // 2  # To avoid overflow in some languages
#         print(mid)
#         if arr[mid] == target:
#             return mid  # Target found, return its index
#         elif arr[mid] < target:
#             low = mid + 1  # Search in the right half
#         else:
#             high = mid - 1  # Search in the left half
    
#     return -1  # Target not found

# # Example Usage
# arr = [1, 3, 5, 7, 9, 11]
# target = 11
# result = binary_search(arr, target)
# print("Target found at index:", result) if result != -1 else print("Target not found.")



def searchInsert(nums, target):

 left = 0
 right = len(nums) -1 
 while left <= right:
     midd = (left + right) // 2
     if nums[midd] == target:
         return midd
     elif nums[midd]<target:
         left = midd +1
     else:
         right = midd -1
 return left
nums = [5]

target = 11
print(searchInsert(nums,11))
        