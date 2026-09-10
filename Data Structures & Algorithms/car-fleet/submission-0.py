class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # farthest from target first
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # this car catches up to the one ahead — merges, no new fleet

        return len(stack)