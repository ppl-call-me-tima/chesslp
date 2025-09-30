from chess import Board

class Chess:
    def __init__(self):
        self.board = Board()
    
    def make_move(self, intent_move):
        move = self.get_move(intent_move)
        
        try:
            self.board.push_san(move)
        except:
            pass
        
        return self.board.fen()
    
    def get_move(self, intent_move):
        piece = intent_move["piece"]
        file = intent_move["file"]
        rank = intent_move["rank"]
        
        if piece == "pawn":
            piece = ""
        elif piece == "knight":
            piece = "N"
        else:
            piece = piece[0].upper()
        
        return f"{piece}{file}{rank}"
