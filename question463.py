class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0 
        for x in range(len(grid)):
            ones = 0
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    ones +=1
                    if x + 1 > len(grid) -1 or grid[x + 1][y] == 0:
                        perimeter += 1
                    if x - 1 < 0 or grid[x - 1][y] == 0:
                        perimeter += 1
                    if y + 1 > len(grid[x]) -1 or grid[x][y+1] == 0:
                        perimeter += 1
                    if y - 1 < 0 or grid[x][y-1] == 0:
                        perimeter +=1
            if perimeter > 0 and ones == 0:
                break
                
                
        return perimeter