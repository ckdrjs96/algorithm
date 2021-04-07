# 위아래 오름차순,왼쪽 오른쪽 오름차순 이므로 아래 왼쪽으로 이동하면서 찾기
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix[0])-1
        col=0
        while row>=0 and col<len(matrix):
            if target < matrix[col][row]:
                row-=1
            elif target > matrix[col][row]:
                col+=1
            else:
                return True
        return False