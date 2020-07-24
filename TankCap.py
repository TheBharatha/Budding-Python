class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = -1
        maxHeight = [[-1,-1] for _ in range(len(height))]
        
        for i in range(len(height)):
            maxHeight[i][0] = maxl
            maxl = max(maxl,height[i])
        maxr = -1
        
        for i in range(len(height)-1,-1,-1):
            maxHeight[i][1] = maxr
            maxr = max(maxr,height[i])
        res = 0
        
        for i in range(len(height)):
            minHeight = min(maxHeight[i])
            if minHeight>height[i]:
                res+=minHeight-height[i]
                
        return res