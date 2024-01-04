#uhhh


from graphics import *

# CONSTS
margin = 25
cell_size = 50
win_width = cell_size * 8 + margin
win_height = cell_size * 8 + margin


# CLASSES
class Board:
    def __init__(self, ranks, files, turn):
        self.ranks = ranks
        self.files = files
        self.turn = turn

class ChessPiece:
    def __init__(self, color, type, posX, posY):
        self.color = color
        self.type = type
        self.pos = (posX * cell_size + (cell_size * 0.5) + margin, posY * cell_size + (cell_size * 0.5) + margin)

        


# FUNCTIONS
def draw_board(win):

    for i in range(board.files):
        for j in range(board.ranks):
            tile = Rectangle(Point(i*cell_size + margin, j*cell_size + margin),
                             Point((i+1)*cell_size + margin, (j+1)*cell_size + margin))
            if j % 2 == 0:
                if not i % 2 == 0:
                    tile.setFill("gray")
                else:
                    tile.setFill("white")
            else:
                if i % 2 == 0:
                    tile.setFill('gray')
                else:
                    tile.setFill("white")
            tile.draw(win)
            rank = 'ABCDEFGH'
    for i in range(len(rank)):
        rank_text = Text(Point(50 * (i +1), 15), f"{rank[i]}")
        rank_text.draw(win)
        rank_text = Text(Point(50 * (i +1), 435), f"{rank[i]}")
        rank_text.draw(win)

    for i in range(8):
        i += 1
        rank_text = Text(Point(15, cell_size * i), f"{i}")
        rank_text.draw(win)
        rank_text = Text(Point(435, cell_size * i), f"{i}")
        rank_text.draw(win)

def handle_click(win, click_point):
    
    if click_point.getX() <= margin or click_point.getX() >= win_width - margin:
        print('Not on board!')
        return None
    elif click_point.getY() <= margin or click_point.getY() >= win_height - margin:
        print('Not on board!')
        return None
    
    x = (click_point.getX() - margin ) // cell_size
    y = (click_point.getY() - margin) // cell_size

    
    
    print([int(x+1), int(y+1)])
    return [int(x+1), int(y+1)]


def set_up_board(win):
    #pawns
    for i in range(8):
        pawn = ChessPiece('white', 'pawn', i, 6)
        draw_piece(win, pawn)
        pawn = ChessPiece('black', 'pawn', i, 1)
        draw_piece(win, pawn)
    #rooks - optimize later
    rook = ChessPiece('black', 'rook', 0, 0)
    draw_piece(win, rook)
    rook = ChessPiece('black', 'rook', 7, 0)
    draw_piece(win, rook)
    rook = ChessPiece('white', 'rook', 0, 7)
    draw_piece(win, rook)
    rook = ChessPiece('white', 'rook', 7, 7)
    draw_piece(win, rook)
    
    

             
def game():
    
    win = GraphWin("HeafChess", win_width + margin, win_height + margin, autoflush = False)
    draw_board(win)
    win.setBackground("lightgray")

    set_up_board(win)


    while not win.isClosed():
        click_point = win.getMouse()
        if win.isClosed() or click_point is None:
            break
        handle_click(win, click_point)


def draw_piece(win, piece):
    if piece.type == 'pawn':
        pawn = Circle(Point(piece.pos[0], piece.pos[1]), 20)
        pawn.setFill(piece.color)
        pawn.draw(win)
    elif piece.type == 'rook':
        rook = Rectangle(Point(piece.pos[0] - 15, piece.pos[1] - 20),
                             Point(piece.pos[0] + 15, (piece.pos[1]+1) + 20))
        rook.setFill(piece.color)
        rook.draw(win)
    elif piece.type == 'knight':
        rook = Rectangle(Point(piece.pos[0] - 15, piece.pos[1] - 20),
                             Point(piece.pos[0] + 15, (piece.pos[1]+1) + 20))
        rook.setFill(piece.color)
        rook.draw(win)
    elif piece.type == 'bishop':
        rook = Rectangle(Point(piece.pos[0] - 15, piece.pos[1] - 20),
                             Point(piece.pos[0] + 15, (piece.pos[1]+1) + 20))
        rook.setFill(piece.color)
        rook.draw(win)
    elif piece.type == 'queen':
        rook = Rectangle(Point(piece.pos[0] - 15, piece.pos[1] - 20),
                             Point(piece.pos[0] + 15, (piece.pos[1]+1) + 20))
        rook.setFill(piece.color)
        rook.draw(win)
    elif piece.type == 'king':
        rook = Rectangle(Point(piece.pos[0] - 15, piece.pos[1] - 20),
                             Point(piece.pos[0] + 15, (piece.pos[1]+1) + 20))
        rook.setFill(piece.color)
        rook.draw(win)


# END FUNCTIONS
if __name__ == '__main__':
    board = Board(8, 8, 0)
    game()
