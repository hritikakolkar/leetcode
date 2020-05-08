"""
Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in th

"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        len_coord=len(coordinates)
        if len_coord==2:return True
        x0,y0=coordinates[0][0],coordinates[0][1]
        x1,y1=coordinates[1][0],coordinates[1][1]
        try :
            slope=(y1-y0)/(x1-x0)
        except:
            return False
        for point in coordinates:
            if point[1]!=slope*(point[0]-x0)+y0:
                return False
        return True
