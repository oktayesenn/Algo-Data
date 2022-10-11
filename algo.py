# def bigon(n):
#     for i in range(0, n):
#         print(i)
# bigon(5)

# def bigon2(n):
#     for i in range (0,n):
#         for j in range (0,n):
#             print(i,j)
# bigon2(5)            


# def nfactorial(n):
#     if n ==0:
#         print("1")
#         return
#     else:
#         for i in range(0,n):
#             print(i)
#             nfactorial(n-1)
# nfactorial(2)            

# from queue import Queue
# from typing import Deque


# Array, List, Stack , Queue, Deque
# import sys

# n = 15 
# myDynamicArray = []
# for i in range(n):
#     myLength = len(myDynamicArray)
#     myByte = sys.getsizeof(myDynamicArray)
#     print(f"Length: {myLength} Byte: {myByte}")
#     myDynamicArray.append(n)



# nums = [1,2,3,4,1,4,2]
# for i in range (len(nums)):
#     if i in nums[]:
#         print("True")
#     else:
#         print("False")

# from queue import LifoQueue
# lifoQueue = LifoQueue()
# lifoQueue.put(1)
# lifoQueue.put(10)
# lifoQueue.put(20)
# lifoQueue


# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

 

# Example 1:

# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.

# class Solution:
#     def calPoints(self, ops: List[str]) -> int:
        
#         # This is O(N) since we are iterating through
#         # Since we are using lifo, stack is great but we can implement it with list as in this example
        
#         stack = []
        
#         for op in ops:
#             if op == "+":
#                 stack.append(stack[-1] + stack[-2])
#             elif op == "C":
#                 stack.pop()
#             elif op == "D":
#                 stack.append(2 * stack[-1])
#             else:
#                 stack.append(int(op))
        
#         return sum(stack)

