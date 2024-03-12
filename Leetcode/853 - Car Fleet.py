class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        inp = []
        
        for i in range(len(position)):
            inp.append([position[i], speed[i]])
        
        inp = sorted(inp, key=lambda x: x[0], reverse=True)
        
        for pos, speed in inp:
            time = (target-pos) / speed
            stack.append(time)

            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
