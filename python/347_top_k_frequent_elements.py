class Solution:
  
  from collections import Counter
  
  def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
    if k == len(nums): # O(1)
      return nums
    
    count = Counter(nums) # O(N)
    
    return heapq.nlargest(k, count.keys(), key=count.get)  # O(N log k)
