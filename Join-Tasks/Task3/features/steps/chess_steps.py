# features/steps/chess_steps.py
import os
import sys

from behave import given, then, when

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)
from chess import ChessBoard


@given("the board is empty except for a Red General at (1, 5)")
def step_given_red_general(context):
    context.chessboard = ChessBoard()
    context.chessboard.place_piece("Red General", (1, 5))


@when("Red moves the General from (1, 5) to (1, 4)")
def step_when_move_general(context):
    context.move = {"piece": "Red General", "from": (1, 5), "to": (1, 4)}
    context.chessboard.move_piece("Red General", (1, 4))


@then("the move is legal")
def step_then_move_legal(context):
    piece = context.move["piece"]
    from_pos = context.move["from"]
    to_pos = context.move["to"]
    assert context.chessboard.is_legal_move(piece, from_pos, to_pos), (
        f"{piece} move should be legal"
    )


# Basic step definitions for walking skeleton
@given("the board is empty except for a Red General at (1, 6)")
def step_given_red_general_16(context):
    context.chessboard = ChessBoard()
    context.chessboard.place_piece("Red General", (1, 6))


@when("Red moves the General from (1, 6) to (1, 7)")
def step_when_move_general_167(context):
    context.move = {"piece": "Red General", "from": (1, 6), "to": (1, 7)}
    context.chessboard.move_piece("Red General", (1, 7))


@then("the move is illegal")
def step_then_move_illegal(context):
    piece = context.move["piece"]
    from_pos = context.move["from"]
    to_pos = context.move["to"]
    assert not context.chessboard.is_legal_move(piece, from_pos, to_pos), (
        f"{piece} move should be illegal"
    )


@given("the board has:")
def step_given_board_has(context):
    context.chessboard = ChessBoard()
    for row in context.table:
        piece_name = row["Piece"]
        position = eval(row["Position"])
        context.chessboard.place_piece(piece_name, position)


@when("Red moves the General from (2, 4) to (2, 5)")
def step_when_move_general_245(context):
    context.move = {"piece": "Red General", "from": (2, 4), "to": (2, 5)}
    context.chessboard.move_piece("Red General", (2, 5))


# Guard step definitions
@given("the board is empty except for a Red Guard at (1, 4)")
def step_given_red_guard_14(context):
    context.chessboard = ChessBoard()
    context.chessboard.place_piece("Red Guard", (1, 4))


@when("Red moves the Guard from (1, 4) to (2, 5)")
def step_when_move_guard_145(context):
    context.move = {"piece": "Red Guard", "from": (1, 4), "to": (2, 5)}
    context.chessboard.move_piece("Red Guard", (2, 5))


@given("the board is empty except for a Red Guard at (2, 5)")
def step_given_red_guard_25(context):
    context.chessboard = ChessBoard()
    context.chessboard.place_piece("Red Guard", (2, 5))


@when("Red moves the Guard from (2, 5) to (2, 6)")
def step_when_move_guard_256(context):
    context.move = {"piece": "Red Guard", "from": (2, 5), "to": (2, 6)}
    context.chessboard.move_piece("Red Guard", (2, 6))


# Rook step definitions
@given("the board is empty except for a Red Rook at (4, 1)")
def step_given_red_rook_41(context):
    context.chessboard = ChessBoard()
    context.chessboard.place_piece("Red Rook", (4, 1))


@when("Red moves the Rook from (4, 1) to (4, 9)")
def step_when_move_rook_419(context):
    context.move = {"piece": "Red Rook", "from": (4, 1), "to": (4, 9)}
    context.chessboard.move_piece("Red Rook", (4, 9))


# Horse step definitions
@given("the board is empty except for a Red Horse at (3, 3)")
def step_given_red_horse_33(context):
    context.chessboard = ChessBoard()
    context.chessboard.place_piece("Red Horse", (3, 3))


@when("Red moves the Horse from (3, 3) to (5, 4)")
def step_when_move_horse_334(context):
    context.move = {"piece": "Red Horse", "from": (3, 3), "to": (5, 4)}
    context.chessboard.move_piece("Red Horse", (5, 4))


# Cannon step definitions
@given("the board is empty except for a Red Cannon at (6, 2)")
def step_given_red_cannon_62(context):
    context.chessboard = ChessBoard()
    context.chessboard.place_piece("Red Cannon", (6, 2))


@when("Red moves the Cannon from (6, 2) to (6, 8)")
def step_when_move_cannon_628(context):
    context.move = {"piece": "Red Cannon", "from": (6, 2), "to": (6, 8)}
    context.chessboard.move_piece("Red Cannon", (6, 8))


# Elephant step definitions
@given("the board is empty except for a Red Elephant at (3, 3)")
def step_given_red_elephant_33(context):
    context.chessboard = ChessBoard()
    context.chessboard.place_piece("Red Elephant", (3, 3))


@when("Red moves the Elephant from (3, 3) to (5, 5)")
def step_when_move_elephant_335(context):
    context.move = {"piece": "Red Elephant", "from": (3, 3), "to": (5, 5)}
    context.chessboard.move_piece("Red Elephant", (5, 5))


@given("the board is empty except for a Red Elephant at (5, 3)")
def step_given_red_elephant_53(context):
    context.chessboard = ChessBoard()
    context.chessboard.place_piece("Red Elephant", (5, 3))


@when("Red moves the Elephant from (5, 3) to (7, 5)")
def step_when_move_elephant_537(context):
    context.move = {"piece": "Red Elephant", "from": (5, 3), "to": (7, 5)}
    context.chessboard.move_piece("Red Elephant", (7, 5))


# Soldier step definitions
@given("the board is empty except for a Red Soldier at (3, 5)")
def step_given_red_soldier_35(context):
    context.chessboard = ChessBoard()
    context.chessboard.place_piece("Red Soldier", (3, 5))


@when("Red moves the Soldier from (3, 5) to (4, 5)")
def step_when_move_soldier_354(context):
    context.move = {"piece": "Red Soldier", "from": (3, 5), "to": (4, 5)}
    context.chessboard.move_piece("Red Soldier", (4, 5))


@when("Red moves the Soldier from (3, 5) to (3, 4)")
def step_when_move_soldier_353(context):
    context.move = {"piece": "Red Soldier", "from": (3, 5), "to": (3, 4)}
    context.chessboard.move_piece("Red Soldier", (3, 4))


@given("the board is empty except for a Red Soldier at (6, 5)")
def step_given_red_soldier_65(context):
    context.chessboard = ChessBoard()
    context.chessboard.place_piece("Red Soldier", (6, 5))


@when("Red moves the Soldier from (6, 5) to (6, 4)")
def step_when_move_soldier_656(context):
    context.move = {"piece": "Red Soldier", "from": (6, 5), "to": (6, 4)}
    context.chessboard.move_piece("Red Soldier", (6, 4))


@when("Red moves the Soldier from (6, 5) to (5, 5)")
def step_when_move_soldier_655(context):
    context.move = {"piece": "Red Soldier", "from": (6, 5), "to": (5, 5)}
    context.chessboard.move_piece("Red Soldier", (5, 5))


# Winning step definitions
@when("Red moves the Rook from (5, 5) to (5, 8)")
def step_when_move_rook_558(context):
    context.move = {"piece": "Red Rook", "from": (5, 5), "to": (5, 8)}
    # 確保有 Red General 在棋盤上（如果沒有的話）
    if "Red General" not in context.chessboard.pieces:
        context.chessboard.place_piece("Red General", (1, 5))  # 放在安全位置
    # 確保有 Black General 在棋盤上（如果沒有的話且目標不是 Black General）
    target_piece = None
    for p, pos in context.chessboard.pieces.items():
        if pos == (5, 8) and p != "Red Rook":
            target_piece = p
            break
    if (
        target_piece != "Black General"
        and "Black General" not in context.chessboard.pieces
    ):
        context.chessboard.place_piece("Black General", (8, 5))  # 放在安全位置
    # 使用 execute_move 來處理吃子和勝負判定
    context.chessboard.execute_move("Red Rook", (5, 5), (5, 8))


@then("Red wins immediately")
def step_then_red_wins(context):
    assert context.chessboard.game_over, "Game should be over"
    assert context.chessboard.get_winner() == "Red", "Red should win"


@then("the game is not over just from that capture")
def step_then_game_continues(context):
    assert not context.chessboard.game_over, "Game should continue"
