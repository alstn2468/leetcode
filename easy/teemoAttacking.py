class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0

        result = duration
        before = timeSeries[0]

        for time in timeSeries[1:]:
            if time - before < duration:
                result += time - before
            else:
                result += duration

            before = time

        return result
