#Binary_Search

sorted_list = [1,5,7,11,14,18,25,32,33,39,42,45]
def binary_search(nums,key):
    low = 0
    high = len(nums) - 1
    while high>=low: #high와 low의 역전까지
        mid = low + (high - low) // 2 #mid 계산
        if nums[mid] == key:
            return mid
        elif nums[mid] > key:          
            high = mid-1
        elif nums[mid] < key:
            low = mid+1

print(binary_search(sorted_list, 18))