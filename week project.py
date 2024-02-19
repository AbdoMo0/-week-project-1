class Solution:
    def insert(self, intervals, new_interval):
        merged_intervals = []
        n = len(intervals)
        i = 0

        while i < n and intervals[i].end < new_interval.start:
            merged_intervals.append(intervals[i])
            i += 1

        while i < n and intervals[i].start <= new_interval.end:
            new_interval.start = min(new_interval.start, intervals[i].start)
            new_interval.end = max(new_interval.end, intervals[i].end)
            i += 1

        merged_intervals.append(new_interval)

        while i < n:
            merged_intervals.append(intervals[i])
            i += 1

        return merged_intervals