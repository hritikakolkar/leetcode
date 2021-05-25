#Find Nearest
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index=-1
        min_dist=1000000
        for idx in range(len(points)):
            xi,yi=points[idx][0],points[idx][1]
            if x==xi or y==yi:
                dist = abs(x-xi)+abs(y-yi)
                if dist < min_dist :
                    min_dist,index=dist,idx
        return index
