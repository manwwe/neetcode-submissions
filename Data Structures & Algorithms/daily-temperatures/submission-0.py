class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for current_index, current_temp in enumerate(temperatures):
            while stack and current_temp > stack[-1][0]:
                pop_temp, pop_index = stack.pop()
                answer[pop_index] = current_index - pop_index

            stack.append([current_temp, current_index])

        return answer
