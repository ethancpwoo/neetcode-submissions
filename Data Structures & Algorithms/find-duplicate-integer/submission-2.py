class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # the obvious solution is get a hashmap and iterate through it
        # if its inside the hashmap, return
        # lets try the without modificationa nd o(1) space. 
        # and O(n)
        # so the way I see it is that we can treat this as a cyclic list
        # with once it reaches the end then it loops back to the beginning
        # if we do a slow and fast pointer it would work. 
        # Lets walk through a 5 element exampel to see when we are guarenteed a solution.
        # actually mathematically speaking, given the period is 5, when do the points meet again? 
        # Is this faster than O(n^2) where we are doing a n search after every element? 
        # i completely misread the question, they give you an array, not a linked list

        # so if there are n + 1 integers in the array where each is between 1 and n, what can we do? 1, nums[1] = 2, nums[2] = 3, nums[3] = 2.. this is a duplicate. 
        slow, fast = 0, 0
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: 
                break
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow