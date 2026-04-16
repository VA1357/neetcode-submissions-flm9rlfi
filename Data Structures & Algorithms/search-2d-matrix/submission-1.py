class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(arr, left, right):
            if left > right:
                return False
            mid = (left + right) // 2
            if target==arr[mid]:
                return True
            elif target > arr[mid]:
                return binary(arr, mid + 1, right)
            else:
                return binary(arr, left, mid-1)
            return False
        
        left = len(matrix)-1
        right = 0

        while right < len(matrix) and matrix[right][0] < target:
            
            right +=1
        while left > 0 and matrix[left][0] > target:
            print(matrix[left][0])
            left -=1
        
        if (left > 0 and right > len(matrix[0])-1) and left==right:
            return True
        else:
        #binary search on all rows to find correct row
            return binary(matrix[left],0,len(matrix[0])-1)
        #binary search within row for answer 

        
