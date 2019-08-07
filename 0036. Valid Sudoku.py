class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):
            d=set()
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] not in d:
                    d.add(board[i][j])
                else:
                    return False
        for i in range(9):
            d=set()
            for j in range(9):
                if board[j][i]==".":
                    continue
                if board[j][i] not in d:
                    d.add(board[j][i])
                else:
                    return False
        for i in [0,3,6]:
            for j in [0,3,6]:
                d=set()
                for m in range(3):
                    for n in range(3):
                        if board[i+m][j+n]==".":
                            continue
                        if board[i+m][j+n] not in d:
                            d.add(board[i+m][j+n])
                        else:
                            return False
                
                
