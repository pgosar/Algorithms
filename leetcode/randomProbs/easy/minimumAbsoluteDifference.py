class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        return arr.sort() or (diff := min(b-a for a, b in zip(arr, arr[1:]))) and None or [[a, b] for a, b in zip(arr, arr[1:]) if b-a == diff]
