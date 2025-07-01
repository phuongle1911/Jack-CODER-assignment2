import pytest
from board import Board
from monte_carlo_player import Monte_carlo_player

@pytest.fixture()
def createBoard():
    print("Creating new board....")
    return Board()

def createPlayer(board):
    print("Creating new MC player....")
    return Monte_carlo_player(board,500)

def test_player_set_board(createBoard):
    player = createPlayer(createBoard)

    createBoard.set_board([ ["-","-","-","-","-","-","-"],
                            ["-","-","-","-","-","-","-"],
                            ["-","-","-","-","-","-","-"],
                            ["-","-","-","-","-","-","-"],
                            ["-","X","-","-","-","-","-"],
                            ["-","O","-","-","-","-","-"]])
    player.update_board(createBoard)
    
    assert player.board.board == [  ["-","-","-","-","-","-","-"],
                                    ["-","-","-","-","-","-","-"],
                                    ["-","-","-","-","-","-","-"],
                                    ["-","-","-","-","-","-","-"],
                                    ["-","X","-","-","-","-","-"],
                                    ["-","O","-","-","-","-","-"]]

def test_player_plays_valid_moves(createBoard):
    player = createPlayer(createBoard)

    for n in range(8):
        assert player.get_move() in createBoard.get_valid_moves()

    createBoard.set_board([ ["-","w","-","z","-","y","u"],
                            ["i","o","p","a","s","d","f"],
                            ["g","h","j","k","l","z","x"],
                            ["q","w","e","r","t","y","u"],
                            ["i","o","p","a","s","d","f"],
                            ["g","h","j","k","l","z","x"]])
    player.update_board(createBoard)
    
    for n in range(8):
        assert player.get_move() in createBoard.get_valid_moves()


    createBoard.set_board([ ["x","w","x","z","x","y","u"],
                            ["i","o","p","a","s","d","f"],
                            ["g","h","j","k","l","z","x"],
                            ["q","w","e","r","t","y","u"],
                            ["i","o","p","a","s","d","f"],
                            ["g","h","j","k","l","z","x"]])
    player.update_board(createBoard)
    assert player.get_move() == -1


def test_player_plays_winning_moves(createBoard):
    player = createPlayer(createBoard)

    createBoard.set_board([ ["-","-","-","-","-","-","-"],
                            ["-","-","-","-","-","-","-"],
                            ["-","X","-","-","-","-","-"],
                            ["-","X","-","-","-","-","-"],
                            ["-","X","-","-","-","-","-"],
                            ["-","O","-","-","-","-","-"]])
    player.update_board(createBoard)
    
    assert player.get_move() == 1

    createBoard.set_board([ ["-","-","-","-","-","-","-"],
                            ["-","-","-","-","-","-","-"],
                            ["-","-","-","-","-","-","-"],
                            ["-","-","-","-","-","-","-"],
                            ["-","-","-","-","-","-","-"],
                            ["-","X","X","X","-","-","-"]])
    player.update_board(createBoard)
    
    assert player.get_move() in [0,4]



