class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(arr, left, right):
            if left > right:
                return False
            mid = (left + right) // 2
            row = mid // len(arr[0])
            col = mid % len(arr[0])
            if target==arr[row][col]:
                return True
            elif target > arr[row][col]:
                return binary(arr, mid + 1, right)
            else:
                return binary(arr, left, mid-1)
            return False
        return binary(matrix,0,len(matrix[0])*len(matrix) -1 )
        #binary search within row for answer 

        
