class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(pm:List[int]):
            #순열을 완성하면 리턴
            if len(nums) == len(pm):
                answer.append(pm)
                return

            #리스트에 없으면 다시 순열 순회
            for e in nums:
                if e not in pm:
                    dfs(pm+[e])

        answer = []
        dfs([])
        return answer