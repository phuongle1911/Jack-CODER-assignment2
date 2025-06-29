import pytest
from board import Board

@pytest.fixture()
def createBoard():
    print("Creating new board....")
    return Board()

def test_new_board(createBoard):
    assert createBoard.get_current_turn() == "O"
    assert createBoard.get_board_state() == [["-" for square in range(7)] for square in range(6)]
    assert createBoard.get_valid_moves() == [0,1,2,3,4,5,6]


def test_valid_moves(createBoard):
    assert createBoard.is_move_valid(-1) == False
    assert createBoard.is_move_valid(99) == False
    assert createBoard.is_move_valid(7) == False
    assert createBoard.is_move_valid(4) == True

    for n in range(6):
        createBoard.play_move(4)
    
    assert createBoard.is_move_valid(4) == False

def test_move(createBoard):
    createBoard.play_move(1)
    assert createBoard.get_board_state() == [["-","-","-","-","-","-","-"],
                                             ["-","-","-","-","-","-","-"],
                                             ["-","-","-","-","-","-","-"],
                                             ["-","-","-","-","-","-","-"],
                                             ["-","-","-","-","-","-","-"],
                                             ["-","O","-","-","-","-","-"]]
    assert createBoard.get_current_turn() == "X"
    createBoard.play_move(1)
    assert createBoard.get_board_state() == [["-","-","-","-","-","-","-"],
                                             ["-","-","-","-","-","-","-"],
                                             ["-","-","-","-","-","-","-"],
                                             ["-","-","-","-","-","-","-"],
                                             ["-","X","-","-","-","-","-"],
                                             ["-","O","-","-","-","-","-"]]
    assert createBoard.get_current_turn() == "O"


