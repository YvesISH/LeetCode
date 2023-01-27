class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m,n=len(mat)-1,len(mat[0])-1
        i,j=0,0
        #find row where the element may exist
        while i<=m:
            mid=(i+m)//2
            if target < mat[mid][0]:
                m=mid-1
            elif target > mat[mid][-1]:
                i=mid+1
            else:
                break
        #find the value in mid-row
        row=mid
        while j<=n:
            mid=(j+n)//2
            if target < mat[row][mid]:
                n=mid-1
            elif target > mat[row][mid]:
                j=mid+1
            else:
                return True
        #if you get here that means element is not there
        return False
