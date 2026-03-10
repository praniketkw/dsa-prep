class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]

        for start, end in intervals:
            lastend = res[-1][1]

            if start>lastend:
                res.append([start,end])
                lastend = end
            else:
                res[-1][0] = min(res[-1][0], start)
                res[-1][1] = max(res[-1][1], end)
                lastend = res[-1][1]
        
        return res