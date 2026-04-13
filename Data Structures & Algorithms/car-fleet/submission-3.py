class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #all positions are unique meaning one car must ALWAYS be in the lead
        #if one car must always be in the lead then we can see which cars will catch up to lead car and which ones wont
        #however that only works for the first fleet and then assumes othger cars are their own fleets
        #but what if multiple multi car fleets form before end?
        #can use a stack to track current fleet amount
        cars = dict(sorted(zip(position, speed), reverse=True))
        stack = []
        ans = len(position)
        for i in cars:
            curr = (target-i)/cars[i]
            if stack:
                if curr <= stack[-1]:
                    ans-=1 
                    continue
            stack.append(curr)
        return ans
            