# def maxSum(array,window):
# 	arr_len = len(array)

# 	if arr_len < window:
# 		print(" == Invalid Window Size == ")
# 		return 
# 	window_val  = sum(array[:window])

# 	max_val = window_val

# 	for i in range(arr_len - window):
# 		window_val = window_val - array[i] + array[i - window]
# 		print(window_val)
# 		max_val = max(max_val,window_val)
		

# 	return max_val

# arr = [1,0,7,3,3,4,7,6,8,5,6,5,7,5,7,9,7,9,8,2,1,2,4]
# win = 3
# print("Max num : ",maxSum(arr,win))

nums = [5,3,2,6,8,1,0,8,0]
num_s = sorted(nums)

print(num_s)