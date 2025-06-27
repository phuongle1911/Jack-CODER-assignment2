import pytest
from board import Board

@pytest.fixture
def createBoard():
    print("Creating new board....")
    return Board()

def test_new_board(createBoard):
    assert createBoard.get_current_turn() == "O"