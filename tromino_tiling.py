def tromino_tiling(n, board=None, top=0, left=0, size=None, hole=None):
    if size is None:
        size = 2 ** n

    if board is None:
        board = [[' ' for _ in range(size)] for _ in range(size)]
        # Προσθήκη της τρύπας
        if hole is None:
            hole = (0, 0)
        board[hole[0]][hole[1]] = 'X'

    # Βασική περίπτωση για n=1
    if n == 1:
        for i in range(2):
            for j in range(2):
                if (top + i, left + j) != hole:
                    board[top + i][left + j] = 'G'
        return board

    # Επέκταση για n = 2
    elif n == 2:
        # Προσωρινή σκληροκοδικοποίηση της τρύπας και των τρομίνων
        tile = 'G'
        board[top + 1][left + 1] = tile  # Κεντρικό τρόμινο
        # Τοποθετούμε τα υπόλοιπα τρόμινο γύρω από την τρύπα
        directions = [(0, 0), (0, 1), (1, 0), (1, 1)]
        colors = ['R', 'B', 'B', 'R']  # Διάφορα χρώματα για απεικόνιση
        index = 0
        for dy, dx in directions:
            if (top + dy, left + dx) != hole:
                board[top + dy][left + dx] = colors[index]
            index += 1
        return board

    # Περαιτέρω επέκταση για n > 2 θα γίνει εδώ

def print_board(board):
    for row in board:
        print(' '.join(row))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python tromino_tiling.py <n>")
        sys.exit(1)
    n = int(sys.argv[1])
    board = tromino_tiling(n)
    print_board(board)
