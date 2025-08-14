# Requirements Document

## Introduction

本專案需要使用行為驅動開發 (BDD) 方式，完成中國象棋遊戲規則的實作。系統需要驗證各種棋子的移動規則，包括將/帥、士/仕、車、馬/傌、炮、相/象、兵/卒等七種棋子的合法移動邏輯，以及勝負判定機制。系統採用 9×10 棋盤座標系統，並嚴格遵循中國象棋的傳統規則。

## Requirements

### Requirement 1

**User Story:** 作為一個象棋玩家，我希望系統能正確驗證將/帥的移動規則，以確保遊戲符合傳統象棋規範

#### Acceptance Criteria

1. WHEN 紅方將帥在宮內移動一格 THEN 系統 SHALL 判定移動合法
2. WHEN 紅方將帥嘗試移出九宮格 THEN 系統 SHALL 判定移動非法
3. WHEN 兩個將帥在同一直線上面對面 THEN 系統 SHALL 判定移動非法

### Requirement 2

**User Story:** 作為一個象棋玩家，我希望系統能正確驗證士/仕的移動規則，以確保遊戲符合傳統象棋規範

#### Acceptance Criteria

1. WHEN 紅方士在宮內斜向移動一格 THEN 系統 SHALL 判定移動合法
2. WHEN 紅方士嘗試直線移動 THEN 系統 SHALL 判定移動非法
3. WHEN 紅方士嘗試移出九宮格 THEN 系統 SHALL 判定移動非法

### Requirement 3

**User Story:** 作為一個象棋玩家，我希望系統能正確驗證車的移動規則，以確保遊戲符合傳統象棋規範

#### Acceptance Criteria

1. WHEN 紅方車在無阻擋路徑上直線移動 THEN 系統 SHALL 判定移動合法
2. WHEN 紅方車嘗試跳過其他棋子移動 THEN 系統 SHALL 判定移動非法
3. WHEN 紅方車移動路徑上有棋子阻擋 THEN 系統 SHALL 判定移動非法

### Requirement 4

**User Story:** 作為一個象棋玩家，我希望系統能正確驗證馬/傌的移動規則，以確保遊戲符合傳統象棋規範

#### Acceptance Criteria

1. WHEN 紅方馬以「日」字形移動且無蹩腳 THEN 系統 SHALL 判定移動合法
2. WHEN 紅方馬移動時被相鄰棋子蹩腳 THEN 系統 SHALL 判定移動非法
3. WHEN 紅方馬嘗試非「日」字形移動 THEN 系統 SHALL 判定移動非法

### Requirement 5

**User Story:** 作為一個象棋玩家，我希望系統能正確驗證炮的移動規則，以確保遊戲符合傳統象棋規範

#### Acceptance Criteria

1. WHEN 紅方炮在無阻擋路徑上移動不吃子 THEN 系統 SHALL 判定移動合法
2. WHEN 紅方炮隔一子吃子 THEN 系統 SHALL 判定移動合法
3. WHEN 紅方炮無隔子直接吃子 THEN 系統 SHALL 判定移動非法
4. WHEN 紅方炮隔多子吃子 THEN 系統 SHALL 判定移動非法

### Requirement 6

**User Story:** 作為一個象棋玩家，我希望系統能正確驗證相/象的移動規則，以確保遊戲符合傳統象棋規範

#### Acceptance Criteria

1. WHEN 紅方相以「田」字形移動且中心點無阻擋 THEN 系統 SHALL 判定移動合法
2. WHEN 紅方相嘗試過河 THEN 系統 SHALL 判定移動非法
3. WHEN 紅方相移動時中心點被阻擋 THEN 系統 SHALL 判定移動非法

### Requirement 7

**User Story:** 作為一個象棋玩家，我希望系統能正確驗證兵/卒的移動規則，以確保遊戲符合傳統象棋規範

#### Acceptance Criteria

1. WHEN 紅方兵未過河時向前移動一格 THEN 系統 SHALL 判定移動合法
2. WHEN 紅方兵未過河時嘗試橫向移動 THEN 系統 SHALL 判定移動非法
3. WHEN 紅方兵過河後橫向移動一格 THEN 系統 SHALL 判定移動合法
4. WHEN 紅方兵過河後嘗試後退 THEN 系統 SHALL 判定移動非法

### Requirement 8

**User Story:** 作為一個象棋玩家，我希望系統能正確判定勝負條件，以確保遊戲能正常結束

#### Acceptance Criteria

1. WHEN 紅方吃掉對方將帥 THEN 系統 SHALL 判定紅方立即獲勝
2. WHEN 紅方吃掉非將帥棋子 THEN 系統 SHALL 判定遊戲繼續進行
3. WHEN 遊戲結束條件達成 THEN 系統 SHALL 正確回報勝負結果

### Requirement 9

**User Story:** 作為一個開發者，我希望系統使用 BDD 開發流程，以確保程式碼品質和測試覆蓋率

#### Acceptance Criteria

1. WHEN 開發過程中 THEN 系統 SHALL 使用 Behave 框架進行 BDD 測試
2. WHEN 程式碼完成後 THEN 系統 SHALL 通過所有 feature 檔案中的 scenario
3. WHEN 開發完成後 THEN 系統 SHALL 使用 Ruff 進行程式碼格式化和檢查
4. WHEN 測試執行時 THEN 系統 SHALL 提供清晰的測試報告和覆蓋率資訊