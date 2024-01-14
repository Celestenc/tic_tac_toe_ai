# Skeleton code: Rough idea of game organization

"""
board = new_board()
run infinitely:
    # Somehow determine player
    player = #get player 1 & 2 somehow

    def render(board)

    def user_input() "get_move"

    coordinates = user_input()

    # Determine where in board to put move and for which player
    def next_move(prev_board, coordinates, player) "make move"

    def get_winner(board)

    if there is a winner:
        print("Player ___ WINS!")
        break

    def is_board_full() "checking for draw"
        print("There's a DRAW, Game Over!")
        break

"""