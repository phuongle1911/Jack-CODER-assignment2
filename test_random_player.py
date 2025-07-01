import pytest
from board import Board
from player import Player

@pytest.fixture()
def createBoard():
    print("Creating new board....")
    return Board()

def createPlayer(board):
    print("Creating new player....")
    return Player(board)

def test_player_plays_valid_moves(createBoard):
    player = createPlayer(createBoard)

    for n in range(10):
        assert player.get_move() in createBoard.get_valid_moves()

    createBoard.set_board([ ["-","w","-","z","-","y","u"],
                            ["i","o","p","a","s","d","f"],
                            ["g","h","j","k","l","z","x"],
                            ["q","w","e","r","t","y","u"],
                            ["i","o","p","a","s","d","f"],
                            ["g","h","j","k","l","z","x"]])
    player.update_board(createBoard)
    
    for n in range(10):
        assert player.get_move() in createBoard.get_valid_moves()


    createBoard.set_board([ ["x","w","x","z","x","y","u"],
                            ["i","o","p","a","s","d","f"],
                            ["g","h","j","k","l","z","x"],
                            ["q","w","e","r","t","y","u"],
                            ["i","o","p","a","s","d","f"],
                            ["g","h","j","k","l","z","x"]])
    player.update_board(createBoard)
    assert player.get_move() == -1






