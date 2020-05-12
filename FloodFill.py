class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if newColor == image[sr][sc]: return image
        q, oldColor = [(sr,sc)], image[sr][sc]
        while q:
            row ,col = q.pop(0)
            if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == oldColor:
                image[row][col] =newColor
                q.append((row+1, col))
                q.append((row-1, col))
                q.append((row, col+1))
                q.append((row, col-1))
        return image
