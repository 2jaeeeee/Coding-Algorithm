class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #중첩함수로 dfs 재귀함수 구현
        def dfs(i:int, s:str):
            #조합이 완료되었을 때 리턴
            if i>=len(digits):
                result.append(s)
                return
            
            #다음 조합 번호로 넘어가기
            for c in numbers[digits[i]]:
                dfs(i+1, s+c)

        #변수 지정
        numbers = {"2":"abc",
                 "3":"def",
                 "4":"ghi",
                 "5":"jkl",
                 "6":"mno",
                 "7":"pqrs",
                 "8":"tuv",
                 "9":"wxyz"}

        result = []
        if len(digits) > 0:
            #dfs 함수 호출
            dfs(0, "")
        return result