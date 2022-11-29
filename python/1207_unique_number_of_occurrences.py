class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = collections.Counter(arr)
        freq_set = set(freq.values())
        return len(freq_set) == len(freq)
