# Design Document

## Overview

本設計文件描述如何使用行為驅動開發 (BDD) 方式完成中國象棋遊戲規則的實作。系統將基於現有的 ChessBoard 類別進行擴展，實現完整的棋子移動規則驗證、勝負判定，並確保所有 BDD scenario 都能通過測試。

系統採用分層架構，將棋盤邏輯、棋子規則、移動驗證和測試步驟分離，確保程式碼的可維護性和可測試性。

## Architecture

### 系統架構圖

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   BDD Tests     │    │   Step Defs     │    │   Chess Logic   │
│  (*.feature)    │◄──►│  (chess_steps)  │◄──►│   (ChessBoard)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │   Piece Rules   │
                                               │   (各棋子類別)    │
                                               └─────────────────┘
```

### 核心組件

1. **BDD 測試層**: Behave 框架執行 feature 檔案中的 scenario
2. **步驟定義層**: 將 Gherkin 語法轉換為 Python 程式碼
3. **遊戲邏輯層**: ChessBoard 類別管理棋盤狀態和移動驗證
4. **棋子規則層**: 各棋子的移動規則實作

## Components and Interfaces

### 1. ChessBoard 類別 (核心棋盤管理)

```python
class ChessBoard:
    def __init__(self):
        self.pieces: Dict[str, Tuple[int, int]] = {}
        self.turn: str = "Red"
        self.game_over: bool = False
        self.winner: Optional[str] = None
    
    # 棋盤管理
    def place_piece(self, name: str, pos: Tuple[int, int]) -> None
    def move_piece(self, name: str, to_pos: Tuple[int, int]) -> None
    def remove_piece(self, name: str) -> None
    def get_piece_at(self, pos: Tuple[int, int]) -> Optional[str]
    
    # 移動驗證
    def is_legal_move(self, piece_name: str, from_pos: Tuple[int, int], to_pos: Tuple[int, int]) -> bool
    def validate_move(self, piece_name: str, from_pos: Tuple[int, int], to_pos: Tuple[int, int]) -> bool
    
    # 勝負判定
    def check_game_over(self) -> bool
    def get_winner(self) -> Optional[str]
```

### 2. 棋子規則驗證方法

每種棋子都有對應的移動規則驗證方法：

```python
# 現有方法 (需要完善)
def is_legal_move_general(self, from_pos, to_pos) -> bool
def is_legal_move_guard(self, from_pos, to_pos) -> bool  
def is_legal_move_rook(self, from_pos, to_pos) -> bool
def is_legal_move_horse(self, from_pos, to_pos) -> bool
def is_legal_move_cannon(self, from_pos, to_pos) -> bool

# 需要新增的方法
def is_legal_move_elephant(self, from_pos, to_pos) -> bool
def is_legal_move_soldier(self, from_pos, to_pos) -> bool
```

### 3. 輔助方法

```python
# 位置驗證
def is_in_red_palace(self, pos: Tuple[int, int]) -> bool
def is_in_black_palace(self, pos: Tuple[int, int]) -> bool
def is_on_red_side(self, pos: Tuple[int, int]) -> bool
def is_on_black_side(self, pos: Tuple[int, int]) -> bool
def has_crossed_river(self, piece_color: str, pos: Tuple[int, int]) -> bool

# 路徑檢查
def is_path_clear(self, from_pos: Tuple[int, int], to_pos: Tuple[int, int]) -> bool
def count_pieces_between(self, from_pos: Tuple[int, int], to_pos: Tuple[int, int]) -> int

# 特殊規則
def generals_face_each_other(self) -> bool
def is_check(self, color: str) -> bool
```

### 4. BDD 步驟定義結構

```python
# Given 步驟 - 設置棋盤狀態
@given('the board is empty except for a {color} {piece} at {position}')
@given('the board has:')

# When 步驟 - 執行移動
@when('{color} moves the {piece} from {from_pos} to {to_pos}')

# Then 步驟 - 驗證結果
@then('the move is legal')
@then('the move is illegal') 
@then('{color} wins immediately')
@then('the game is not over just from that capture')
```

## Data Models

### 棋盤座標系統
- 使用 (row, col) 座標系統
- Row 1-10: Row 1 為紅方底線，Row 10 為黑方底線
- Col 1-9: Col 1 為紅方視角最左側

### 棋子表示
```python
# 棋子名稱格式: "{Color} {Type}"
# 例如: "Red General", "Black Horse", "Red Soldier"

PIECE_TYPES = {
    "General": "將/帥",
    "Guard": "士/仕", 
    "Rook": "車",
    "Horse": "馬/傌",
    "Cannon": "炮",
    "Elephant": "相/象",
    "Soldier": "兵/卒"
}

COLORS = ["Red", "Black"]
```

### 移動記錄
```python
@dataclass
class Move:
    piece_name: str
    from_pos: Tuple[int, int]
    to_pos: Tuple[int, int]
    is_capture: bool
    captured_piece: Optional[str]
    is_legal: bool
```

## Error Handling

### 1. 移動驗證錯誤
- 非法位置座標 (超出 1-10, 1-9 範圍)
- 棋子不存在於指定位置
- 違反棋子移動規則
- 移動後造成將帥相望

### 2. 測試執行錯誤
- Step definition 找不到對應的實作
- 棋盤狀態設置錯誤
- 斷言失敗時提供清晰的錯誤訊息

### 3. 錯誤處理策略
```python
class ChessError(Exception):
    """象棋遊戲基礎異常"""
    pass

class IllegalMoveError(ChessError):
    """非法移動異常"""
    pass

class InvalidPositionError(ChessError):
    """無效位置異常"""
    pass
```

## Testing Strategy

### 1. BDD 測試流程

**Phase 1: Walking Skeleton**
- 建立基本的 Behave 測試環境
- 實作一個最簡單的 scenario 並確保能執行
- 驗證測試框架正常運作

**Phase 2: 逐步實作 Scenarios**
- 一次選擇一個 scenario 實作
- 其他 scenario 暫時 ignore
- 遵循 Red-Green-Refactor 循環：
  1. 寫 step definitions，讓測試失敗 (Red)
  2. 實作最少程式碼讓測試通過 (Green)  
  3. 重構程式碼保持測試通過 (Refactor)

**Phase 3: 程式碼品質**
- 使用 Ruff 進行 linting 和 formatting
- 確保所有測試通過
- 檢查程式碼覆蓋率

### 2. 測試分類

**按棋子類型分組:**
- @General: 將/帥移動規則
- @Guard: 士/仕移動規則  
- @Rook: 車移動規則
- @Horse: 馬/傌移動規則
- @Cannon: 炮移動規則
- @Elephant: 相/象移動規則
- @Soldier: 兵/卒移動規則
- @Winning: 勝負判定規則

**測試執行策略:**
```bash
# 執行所有測試
behave features/chess.feature

# 執行特定標籤的測試
behave features/chess.feature --tags=@General

# 執行單一 scenario
behave features/chess.feature:line_number
```

### 3. 測試資料管理

使用 Behave 的 context 物件管理測試狀態：
```python
# context.chessboard: ChessBoard 實例
# context.move: 當前移動資訊
# context.table: Given 步驟中的表格資料
```

### 4. 持續整合考量

- 每次 commit 都要通過所有 BDD 測試
- 程式碼必須通過 Ruff 檢查
- 測試執行時間應保持在合理範圍內
- 提供清晰的測試報告和失敗原因

## Implementation Notes

### 1. 現有程式碼分析
- ChessBoard 類別已有基本結構
- 部分棋子規則已實作 (General, Guard, Rook, Horse, Cannon)
- 需要補充 Elephant 和 Soldier 的規則
- 需要完善勝負判定邏輯

### 2. 程式碼改進重點
- 統一方法命名規範
- 加強錯誤處理和邊界條件檢查
- 改善程式碼可讀性和維護性
- 確保所有方法都有適當的文檔

### 3. BDD 最佳實踐
- Step definitions 應該簡潔明確
- 避免在 step 中包含複雜的業務邏輯
- 使用描述性的變數名稱
- 保持 scenario 的獨立性

### 4. 效能考量
- 棋盤狀態檢查應該高效
- 避免不必要的重複計算
- 合理使用快取機制