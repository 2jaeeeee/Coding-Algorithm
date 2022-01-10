from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs 중첩함수 정의
        def dfs(i:int, j:int):
            if i < 0 or j < 0 or \
                    i >= len(grid) or j >= len(grid[0]) or \
                    grid[i][j] == '0':
                return
            grid[i][j] = '0' #방문한 노드는 0으로 변경

            #동서남북 방향으로 순회
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        visit = []
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if [i, j] not in visit and grid[i][j] == '1':
                    dfs(i, j)
                    count += 1 #순회가 끝난 후 횟수 up

        return count