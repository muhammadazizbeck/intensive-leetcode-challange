class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        # counter = 0
        # for operation in operations:
        #     if operation=="--X" or operation=="X--":
        #         counter -= 1
        #     else:
        #         counter += 1
        # return counter

        # negative=[ret for ret in operations if ret=="--X" or ret=="X--"]
        # positive=[ret for ret in operations if ret=="++X" or ret=="X++"]
        # return len(positive)-len(negative) 

        total = 0
        for op in operations:
            if "-" in op:
                total -= 1
            else:
                total += 1
        return total
            