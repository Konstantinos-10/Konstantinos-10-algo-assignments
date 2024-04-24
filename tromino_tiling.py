def tromino_tiling(n, board=None, top=0, left=0, size=None, hole=None):
    if size is None:
        size = 2 ** n

    if board is None:
        board = [[' ' for _ in range(size)] for _ in range(size)]
        # Προσθήκη της τρύπας
        if hole is None:
            hole = (0, 0)
        board[hole[0]][hole[1]] = 'X'

    # Βασική περίπτωση
    if n == 1:
        tile = 1
        for i in range(2):
            for j in range(2):
                if (top + i, left + j) != hole:
                    board[top + i][left + j] = 'G'
        return board

    # Αυτός ο κώδικας θα επεκταθεί στις επόμενες μέρες

def print_board(board):
    for row in board:
        print(' '.join(row))

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])
    board = tromino_tiling(n)
    print_board(board)
