"""
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.
"""
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        """
        Area=0.5*(x1(y2−y3)+x2(y3−y1)+x3(y1−y2))
        """
        return (0.5*(points[0][0]*(points[1][1]-points[2][1])+points[1][0]*(points[2][1]-points[0][1])+points[2][0]*(points[0][1]-points[1][1])))!=0
