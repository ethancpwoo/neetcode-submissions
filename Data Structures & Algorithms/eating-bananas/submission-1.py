class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # so my immediate thoughts
        # h is the amount of hours and the average time you can spend on a pile is 
        # h/len(pile) = allowed time per pile
        # if any pile exceeds the allowed time, then we have to increase our eating rate
        # The issue with this is that it assumes that if we finish fast on one pile, then we cannot allot that time to another pile. 
        
        # What is another solu? Does 
        # So the guarentee is that you have at least an hour per pile. 
        # this is hard
        # therefore the upper bound is the max of the array. We can check if we have any budge to allocate more hours to lower the rate
        # once we have the upper bound, what is the best bang for our buck for an extra hour? 

        # piles = sorted(piles)
        # cur_time = len(piles)
        # spent_time = [1] * len(piles)
        # ks = piles
        # while cur_time >= h:
        #     limiter = argmax(ks)
        #     ks[limiter] = math.ceil(piles[limiter]/spent_time[limiter])
        #     spent_time[limiter] += 1
        #     cur_time += 1
        # return argmax(ks)

        # I ran this solution by an LLM and they said conceptually it is correct, but the time limits would stop this from working. The correct sol is O(n log m) and my solution is 
        # O ((h-n) log n). I mean the h constraint is dumb because 10e9 is 100,000 years and 
        # Koko is dead a million times over. 

        # personally I dont like the "brute force" since you just have a upper bound and guess over the remaining possibilities as a check. 

        import math
        l, r = 1, max(piles)

        while l < r: 
            mid = (l+r)//2
            if sum(math.ceil(p/mid) for p in piles) <= h:
                r = mid
            else:
                l = mid + 1
        return l


        
            
