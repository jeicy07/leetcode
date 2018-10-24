class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        hashmap, heap = {}, []
        for word in words:
            hashmap[word] = -1 if word not in hashmap else hashmap[word] - 1
        
        for word in hashmap:
            heap.append((hashmap[word], word))
        
        heapq.heapify(heap)
        
        res = [heapq.heappop(heap)[1] for s in range(0,k)]
        
        return res