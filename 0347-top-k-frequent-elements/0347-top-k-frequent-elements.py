class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time Complexity O(k log n)

        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        heap = []

        for num, f in freq.items():
            heapq.heappush(heap, (f, num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans

        