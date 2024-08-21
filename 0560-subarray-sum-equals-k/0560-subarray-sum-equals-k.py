class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:

		result = 0 
		prefix_sum = 0
		dictionary = {0 : 1}

		for num in nums:
		
			prefix_sum = prefix_sum + num

			if prefix_sum - k in dictionary:
			
				result = result + dictionary[prefix_sum - k]

			if prefix_sum not in dictionary:
			
				dictionary[prefix_sum] = 1
			else:
				dictionary[prefix_sum] = dictionary[prefix_sum] + 1

		return result