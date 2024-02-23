
def run_two(board, line_x, line_y):
    print(board)
    
"""t = 5

line_x = 4

for _ in range(t):
    board = []
    for y in range(line_x):
        board.append(list(map(int, input().split())))
    run_two(board, line_x, len(board))"""

board = [[2, 64, 4, 32],[8, 16, 8, 4],[4, 32, 4, 0],[2, 2, 0, 0]]

run_two(board, 4, 4)
