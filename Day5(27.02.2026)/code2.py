#target

'''
example 1
nums = [2,7,11,15] , target = 9
output = [0 ,1]
explain = nums[0] + nums[1] == 9
'''

def twoNum(nums , target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return -1             
            
nums = [11,15,2,7]
target = 9
print(twoNum(nums , target))