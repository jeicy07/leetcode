class Solution:
    import math
    def maxNumberOfBalloons(self, text: str) -> int:
        result = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for i in text:
            if i == "l" or i == "o":
                result[i] += 0.5
            elif i in result:
                result[i] += 1
    
        return math.floor(result[min(result, key=result.get)])