# Problem Statement
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
#  and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
# Example 2:
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# This Method will Sort the Intervals depending upon their starting time and then we know that
def mergeInterValUsingSorting(arr):
    pass



# This Method will Pick one element at once and then it will traverse complete array to merge intervals.
# Time Complexity of this method will be O(N*N) as we are running two loops.
def mergeIntervalsBruteForce(arr):

    size =len(arr)
    # Outer Loop to Pick first element and compare in complete array
    for i in range(0,size):
        if arr[i]:

            curr = arr[i]
            for j in range(i+1,size):
                if curr[1] >= arr[j][0]:
                   curr[1] = max(arr[j][1],curr[1])  # To get the maximum interval
                   arr[j] = [-1,-1]
            arr[i] = curr

    # To remove the None Object
    result = []
    for i in arr:
        if i[0] !=-1: result.append(i)

    return result


intervals = [[1,3],[2,4],[5,7],[6,8]]
print(mergeIntervalsBruteForce(intervals))