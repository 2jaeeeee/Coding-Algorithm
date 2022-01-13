from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev = []

        def dfs(elements):
            #순열이 완성되면 결과에 저장
            if len(elements) == 0:
                results.append(prev[:])

            #입력한 요소들 중 하나씩 dfs 호출
            for e in elements:
                next = elements[:]
                next.remove(e)

                prev.append(e)
                dfs(next)
                prev.pop()

        dfs(nums)
        return results


