class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        s,e = newInterval

        for i in range(len(intervals)):
            if e<intervals[i][0]:
                res.append([s,e])
                return res+intervals[i:]
            
            elif s>intervals[i][1]:
                res.append(intervals[i])
            
            else:
                s = min(s, intervals[i][0])
                e = max(e, intervals[i][1])
        
        res.append([s,e])
        return res
                



        