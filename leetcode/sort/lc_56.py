class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # print(intervals)
        # sorted(intervals,key=lambda)
        intervals.sort(key=lambda x:x[0])
        a=intervals[0][0]
        b=intervals[0][1]
        ans=[]
        for first,second in intervals[1:]:
            if b<first:
                ans.append([a,b])
                a=first
                b=second
            elif b >= first:
                if b<second:
                    b=second
        ans.append([a,b])

        return ans