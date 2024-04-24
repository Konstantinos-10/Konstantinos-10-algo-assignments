def tromino_tiling(n, board=None, top=0, left=0, size=None, hole=None):
    if size is None:
        size = 2 ** n

    if board is None:
        board = [[' ' for _ in range(size)] for _ in range(size)]
        if hole is None:
            hole = (0, 0)
        board[hole[0]][hole[1]] = 'X'

    if n == 1:
        for i in range(2):
            for j in range(2):
                if (top + i, left + j) != hole:
                    board[top + i][left + j] = 'G'
        return board

    elif n == 2:
        directions = [(0, 0), (0, 1), (1, 0), (1, 1)]
        colors = ['R', 'B', 'B', 'R']
        index = 0
        for dy, dx in directions:
            if (top + dy, left + dx) != hole:
                board[top + dy][left + dx] = colors[index]
            index += 1
        return board

    else:
        sub_size = size // 2
        # Βρίσκουμε τη θέση για την τρύπα στο κέντρο του μεγαλύτερου τετραγώνου
        middle = (top + sub_size - 1, left + sub_size - 1)
        # Θέτουμε τρόμινο στο κέντρο που καλύπτει τρία από τα τέσσερα κεντρικά τετράγωνα
        for dy, dx in [(0, 0), (0, 1), (1, 0)]:
            board[middle[0] + dy][middle[1] + dx] = 'G'
        # Αναδρομική κλήση για κάθε τεταρτημόριο
        # Εξαίρεση: μεταφέρουμε την τρύπα στο κατάλληλο τεταρτημόριο
        for i in range(2):
            for j in range(2):
                new_top = top + i * sub_size
                new_left = left + j * sub_size
                new_hole = (middle[0] + i, middle[1] + j) if board[middle[0] + i][middle[1] + j] == 'G' else hole
                tromino_tiling(n-1, board, new_top, new_left, sub_size, new_hole)
        return board

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
