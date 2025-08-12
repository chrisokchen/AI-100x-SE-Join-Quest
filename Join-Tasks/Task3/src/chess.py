# src/chess.py


class ChessBoard:
    """中國象棋棋盤類別，實作所有棋子的移動規則和遊戲邏輯"""
    
    def is_legal_move_cannon(self, from_pos, to_pos):
        fr, fc = from_pos
        tr, tc = to_pos
        # 只能橫或直移動
        if fr != tr and fc != tc:
            return False
        # 計算路徑上有幾個棋子
        count = 0
        if fr == tr:
            rng = range(min(fc, tc) + 1, max(fc, tc))
            for c in rng:
                for p, pos in self.pieces.items():
                    if pos == (fr, c):
                        count += 1
        else:
            rng = range(min(fr, tr) + 1, max(fr, tr))
            for r in rng:
                for p, pos in self.pieces.items():
                    if pos == (r, fc):
                        count += 1
        # 目標格是否有棋子
        target = None
        for p, pos in self.pieces.items():
            if pos == to_pos and p != "Red Cannon":
                target = p
                break
        if target:
            return count == 1  # 吃子必須跳一個
        return count == 0  # 不吃子不能跳

    def is_legal_move_horse(self, from_pos, to_pos):
        fr, fc = from_pos
        tr, tc = to_pos
        dr, dc = tr - fr, tc - fc
        # 必須日字形
        if (abs(dr), abs(dc)) not in [(2, 1), (1, 2)]:
            return False
        # 檢查蹩馬腿
        if abs(dr) == 2:
            leg = (fr + dr // 2, fc)
        else:
            leg = (fr, fc + dc // 2)
        for p, pos in self.pieces.items():
            if pos == leg:
                return False
        return True

    def is_legal_move_rook(self, from_pos, to_pos):
        fr, fc = from_pos
        tr, tc = to_pos
        # 只能橫或直移動
        if fr != tr and fc != tc:
            return False
        # 路徑上不可有其他棋子
        if fr == tr:
            rng = range(min(fc, tc) + 1, max(fc, tc))
            for c in rng:
                for p, pos in self.pieces.items():
                    if pos == (fr, c):
                        return False
        else:
            rng = range(min(fr, tr) + 1, max(fr, tr))
            for r in rng:
                for p, pos in self.pieces.items():
                    if pos == (r, fc):
                        return False
        return True

    def is_legal_move_guard(self, from_pos, to_pos):
        # 只允許斜對角一步且在宮內
        if not self.is_in_red_palace(from_pos) or not self.is_in_red_palace(to_pos):
            return False
        fr, fc = from_pos
        tr, tc = to_pos
        return abs(fr - tr) == 1 and abs(fc - tc) == 1

    def generals_face_each_other(self):
        red = self.pieces.get("Red General")
        black = self.pieces.get("Black General")
        if not red or not black:
            return False
        if red[1] != black[1]:
            return False
        min_row = min(red[0], black[0])
        max_row = max(red[0], black[0])
        for p, pos in self.pieces.items():
            if (
                p not in ("Red General", "Black General")
                and pos[1] == red[1]
                and min_row < pos[0] < max_row
            ):
                return False
        return True

    def __init__(self):
        self.pieces = {}
        self.game_over = False
        self.winner = None

    def place_piece(self, name, pos):
        self.pieces[name] = pos

    def move_piece(self, name, to_pos):
        self.pieces[name] = to_pos

    def is_in_red_palace(self, pos):
        row, col = pos
        return 1 <= row <= 3 and 4 <= col <= 6

    def is_legal_move_general(self, from_pos, to_pos):
        # 只能在九宮格內，且只能橫或直移動一格
        if not self.is_in_red_palace(to_pos):
            return False
        fr, fc = from_pos
        tr, tc = to_pos
        if not self.is_in_red_palace(from_pos):
            return False
        if abs(fr - tr) + abs(fc - tc) != 1:
            return False
        # 移動後不可將帥相望
        orig = self.pieces.get("Red General")
        self.pieces["Red General"] = to_pos
        face = self.generals_face_each_other()
        self.pieces["Red General"] = orig
        if face:
            return False
        return True

    def is_legal_move_elephant(self, from_pos, to_pos):
        fr, fc = from_pos
        tr, tc = to_pos
        # 必須田字形移動 (2步對角線)
        if abs(fr - tr) != 2 or abs(fc - tc) != 2:
            return False
        # 不能過河 (紅方象不能超過第5行)
        if tr > 5:
            return False
        # 檢查中心點是否被阻擋
        center_r = (fr + tr) // 2
        center_c = (fc + tc) // 2
        for p, pos in self.pieces.items():
            if pos == (center_r, center_c):
                return False
        return True

    def is_legal_move_soldier(self, from_pos, to_pos):
        fr, fc = from_pos
        tr, tc = to_pos

        # 只能移動一格
        if abs(fr - tr) + abs(fc - tc) != 1:
            return False

        # 未過河前只能向前
        if fr <= 5:  # 未過河
            # 只能向前移動 (row 增加)
            if tr != fr + 1 or tc != fc:
                return False
        else:  # 已過河
            # 可以向前或橫向移動，但不能後退
            if tr < fr:  # 後退
                return False
            if tr == fr:  # 橫向移動
                if abs(tc - fc) != 1:
                    return False
            elif tr == fr + 1:  # 向前移動
                if tc != fc:
                    return False
            else:
                return False

        return True

    def check_game_over(self):
        """檢查遊戲是否結束"""
        # 檢查是否有將帥被吃掉
        red_general = self.pieces.get("Red General")
        black_general = self.pieces.get("Black General")

        if not red_general:
            self.game_over = True
            self.winner = "Black"
            return True
        if not black_general:
            self.game_over = True
            self.winner = "Red"
            return True

        return False

    def get_winner(self):
        """取得勝利者"""
        return self.winner

    def execute_move(self, piece_name, from_pos, to_pos):
        """執行移動並檢查是否吃子"""
        # 檢查目標位置是否有棋子
        captured_piece = None
        for p, pos in self.pieces.items():
            if pos == to_pos and p != piece_name:
                captured_piece = p
                break

        # 移動棋子
        self.pieces[piece_name] = to_pos

        # 如果有吃子，移除被吃的棋子
        if captured_piece:
            del self.pieces[captured_piece]

        # 檢查遊戲是否結束
        self.check_game_over()

        return captured_piece

    def is_legal_move(self, piece_name, from_pos, to_pos):
        """統一的移動驗證介面"""
        if "General" in piece_name:
            return self.is_legal_move_general(from_pos, to_pos)
        if "Guard" in piece_name:
            return self.is_legal_move_guard(from_pos, to_pos)
        if "Rook" in piece_name:
            return self.is_legal_move_rook(from_pos, to_pos)
        if "Horse" in piece_name:
            return self.is_legal_move_horse(from_pos, to_pos)
        if "Cannon" in piece_name:
            return self.is_legal_move_cannon(from_pos, to_pos)
        if "Elephant" in piece_name:
            return self.is_legal_move_elephant(from_pos, to_pos)
        if "Soldier" in piece_name:
            return self.is_legal_move_soldier(from_pos, to_pos)
        return False
