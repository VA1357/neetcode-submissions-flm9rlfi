from collections import defaultdict

class TimeMap:

    def __init__(self):
        #use name and time as tuple key, then  sort by time in the get function and binary search till we get to the time?
        self.timeset = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeset[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.timeset[key]:
            return ""
        arr = self.timeset[key]
        l = 0
        r = len(arr)-1
        ans = -1
        while l <= r:
            mid = (l + r)//2
            if arr[mid][0] == timestamp:
                return self.timeset[key][mid][1]
            elif self.timeset[key][mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
                ans = max(ans, mid) 
        if ans==-1:
            return ""
        return self.timeset[key][ans][1]
            