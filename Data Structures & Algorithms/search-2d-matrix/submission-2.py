class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bot = 0, len(matrix)-1

        
        while top <= bot:
            m = (top+bot)//2
            
            if matrix[m][-1] < target:
                top=m+1
            elif matrix[m][0] > target:
                bot = m-1
            else:
                l,r=0,len(matrix[m])-1
                while l<=r:
                    mid = (l+r)//2
                    
                    if target > matrix[m][mid]:
                        l=mid+1
                    elif target < matrix[m][mid]:
                        r=mid-1
                    else:
                        return True
                return False
        return False

