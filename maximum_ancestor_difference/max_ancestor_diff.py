'''
Source: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor

Computational complexity: Very bad. I prioritized readability over optimization for future reference.
Time complexity: O(n) where n is the number of nodes
Space complexity: O(n) ``

Notes:
CamelCase naming convention is set by the leetcode problem.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root) -> int:
        leftAnswer = rightAnswer = []
        if root.left != None:
            leftGoal = [min(root.left.val, root.val), max(root.left.val, root.val)]
            leftAnswer = Solution.myApproach(root.left, leftGoal)
        if root.right != None:
            rightGoal = [min(root.right.val, root.val), max(root.right.val, root.val)]
            rightAnswer = Solution.myApproach(root.right, rightGoal)
        
        if len(leftAnswer) == 0: # root.left == None
            if len(rightAnswer) == 0: # root.right == None
                return 0
            return rightAnswer[1] - rightAnswer[0]
        elif len(rightAnswer) == 0:
            return leftAnswer[1] - leftAnswer[0]
        else:
            return max(abs(leftAnswer[1] - leftAnswer[0]), abs(rightAnswer[1] - rightAnswer[0]))
    
    # Assumes tree is at least 2 levels deep, therefore goalList != []
    @staticmethod
    def myApproach(node, goalList) -> list:
        goalList = [min(node.val, goalList[0]), max(node.val, goalList[1])]
        tempGoalListLeft = []
        if node.left != None:
            tempGoalListLeft = Solution.myApproach(node.left, goalList=goalList)

        tempGoalListRight = []
        if node.right != None:
            tempGoalListRight= Solution.myApproach(node.right, goalList=goalList)

        tempGreatestDifference = []
        # goalList will not be None.
        if len(tempGoalListLeft) == 0:
            if len(tempGoalListRight) == 0:
                return goalList
            tempGreatestDifference = tempGoalListRight
        elif len(tempGoalListRight) == 0:
            tempGreatestDifference = tempGoalListLeft
        else:
            tempGreatestDifference = tempGoalListLeft if tempGoalListLeft[1] - tempGoalListLeft[0] > tempGoalListRight[1] - tempGoalListRight[0] else tempGoalListRight
        return tempGreatestDifference if tempGreatestDifference[1] - tempGreatestDifference[0] > goalList[1] - goalList[0] else goalList
    
    @staticmethod # Initial approach. Doesn't work.
    def somethingelse(node) -> list:
        greatestLeft = []
        if node.left != None:
            greatestLeft = sorted([node.val, node.left.val])
            
            glb = Solution.myApproach(node.left)
            if len(glb) > 0:
                temp = glb
                if type(glb[0]) == int: # [1, 2]
                    if node.val < glb[0]:
                        temp = [node.val, glb[1]]
                    elif node.val > greatestLeft[1]:
                        temp = [glb[0], node.val]
                    else:
                        temp = glb
                else: # [[4, 5], [1, 3]]
                    for lst in glb:
                        temp = lst
                        if node.val < temp[0]:
                            temp = [node.val, temp[1]]
                        elif node.val > greatestLeft[1]:
                            temp = [temp[0], node.val]
                        else:
                            pass
                        if parentChild[1]-parentChild[0] > temp[1]-temp[0]:
                            greatestLeft = parentChild
                
                if greatestLeft[1]-greatestLeft[0] < glb[1]-glb[0]:
                    greatestLeft = greatestLeft
                else:
                    greatestLeft = glb
        
        greatestRight = []
        if node.right != None:
            parentChild = sorted([node.val, node.right.val])
            greatestRight = Solution.myApproach(node.right)
            print(node.right.val, greatestRight)
            if len(greatestRight) > 0:
                if node.val < greatestRight[0]:
                    greatestRight = [node.val, greatestRight[1]]
                elif node.val > greatestRight[1]:
                    greatestRight = [greatestRight[0], node.val]
                else:
                    pass
                if parentChild[1]-parentChild[0] > greatestRight[1]-greatestRight[0]:
                    greatestRight = parentChild
            else:
                greatestRight = parentChild
        
        if len(greatestLeft) == 0:
            if len(greatestRight) == 0:
                return greatestLeft # []
            return greatestRight
        if len(greatestRight) == 0:
            return greatestLeft
        return [greatestLeft, greatestRight]
