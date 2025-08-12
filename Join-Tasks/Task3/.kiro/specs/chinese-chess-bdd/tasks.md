# Implementation Plan

- [x] 1. 建立 BDD Walking Skeleton

  - 設置 Behave 測試環境和基本配置
  - 建立最簡單的 scenario 測試並確保能執行
  - 驗證測試框架與現有程式碼的整合
  - _Requirements: 9.1, 9.2_

- [x] 2. 實作 General (將/帥) 相關 scenarios

- [x] 2.1 實作 General 在宮內移動的合法性驗證

  - 完善 `is_legal_move_general` 方法處理宮內移動
  - 實作對應的 step definitions
  - 確保 "Red moves the General within the palace (Legal)" scenario 通過
  - _Requirements: 1.1_

- [x] 2.2 實作 General 移出宮外的非法性驗證

  - 加強 `is_legal_move_general` 方法的邊界檢查
  - 實作對應的 step definitions
  - 確保 "Red moves the General outside the palace (Illegal)" scenario 通過
  - _Requirements: 1.2_

- [x] 2.3 實作將帥相望的非法性驗證

  - 完善 `generals_face_each_other` 方法
  - 實作複雜棋盤狀態的 step definitions
  - 確保 "Generals face each other on the same file (Illegal)" scenario 通過
  - _Requirements: 1.3_

- [x] 3. 實作 Guard (士/仕) 相關 scenarios

- [x] 3.1 實作 Guard 宮內斜向移動的合法性驗證

  - 完善 `is_legal_move_guard` 方法處理斜向移動
  - 實作對應的 step definitions
  - 確保 "Red moves the Guard diagonally in the palace (Legal)" scenario 通過
  - _Requirements: 2.1_

- [x] 3.2 實作 Guard 直線移動的非法性驗證

  - 加強 `is_legal_move_guard` 方法的移動方向檢查
  - 實作對應的 step definitions
  - 確保 "Red moves the Guard straight (Illegal)" scenario 通過
  - _Requirements: 2.2_

- [x] 4. 實作 Rook (車) 相關 scenarios

- [x] 4.1 實作 Rook 直線移動的合法性驗證

  - 完善 `is_legal_move_rook` 方法處理清晰路徑
  - 實作對應的 step definitions
  - 確保 "Red moves the Rook along a clear rank (Legal)" scenario 通過
  - _Requirements: 3.1_

- [x] 4.2 實作 Rook 跳躍移動的非法性驗證

  - 加強 `is_legal_move_rook` 方法的路徑阻擋檢查
  - 實作複雜棋盤狀態的 step definitions
  - 確保 "Red moves the Rook and attempts to jump over a piece (Illegal)" scenario 通過
  - _Requirements: 3.2, 3.3_

- [x] 5. 實作 Horse (馬/傌) 相關 scenarios

- [x] 5.1 實作 Horse 日字形移動的合法性驗證

  - 完善 `is_legal_move_horse` 方法處理無阻擋的日字形移動
  - 實作對應的 step definitions
  - 確保 "Red moves the Horse in an 'L' shape with no block (Legal)" scenario 通過
  - _Requirements: 4.1_

- [x] 5.2 實作 Horse 蹩腳的非法性驗證

  - 加強 `is_legal_move_horse` 方法的蹩腳檢查
  - 實作複雜棋盤狀態的 step definitions
  - 確保 "Red moves the Horse and it is blocked by an adjacent piece (Illegal)" scenario 通過
  - _Requirements: 4.2_

- [x] 6. 實作 Cannon (炮) 相關 scenarios

- [x] 6.1 實作 Cannon 無阻擋移動的合法性驗證

  - 完善 `is_legal_move_cannon` 方法處理無阻擋路徑移動
  - 實作對應的 step definitions
  - 確保 "Red moves the Cannon like a Rook with an empty path (Legal)" scenario 通過
  - _Requirements: 5.1_

- [x] 6.2 實作 Cannon 隔一子吃子的合法性驗證

  - 完善 `is_legal_move_cannon` 方法處理隔子吃子邏輯
  - 實作複雜棋盤狀態的 step definitions
  - 確保 "Red moves the Cannon and jumps exactly one screen to capture (Legal)" scenario 通過
  - _Requirements: 5.2_

- [x] 6.3 實作 Cannon 無隔子吃子的非法性驗證

  - 加強 `is_legal_move_cannon` 方法的隔子檢查
  - 實作對應的 step definitions
  - 確保 "Red moves the Cannon and tries to jump with zero screens (Illegal)" scenario 通過
  - _Requirements: 5.3_

- [x] 6.4 實作 Cannon 隔多子吃子的非法性驗證

  - 加強 `is_legal_move_cannon` 方法的多隔子檢查
  - 實作複雜棋盤狀態的 step definitions
  - 確保 "Red moves the Cannon and tries to jump with more than one screen (Illegal)" scenario 通過
  - _Requirements: 5.4_

- [x] 7. 實作 Elephant (相/象) 相關 scenarios

- [x] 7.1 建立 Elephant 移動規則驗證方法

  - 實作 `is_legal_move_elephant` 方法處理田字形移動
  - 實作對應的 step definitions
  - 確保 "Red moves the Elephant 2-step diagonal with a clear midpoint (Legal)" scenario 通過
  - _Requirements: 6.1_

- [x] 7.2 實作 Elephant 過河的非法性驗證

  - 加強 `is_legal_move_elephant` 方法的過河檢查
  - 實作對應的 step definitions
  - 確保 "Red moves the Elephant and tries to cross the river (Illegal)" scenario 通過
  - _Requirements: 6.2_

- [x] 7.3 實作 Elephant 中心點阻擋的非法性驗證

  - 加強 `is_legal_move_elephant` 方法的中心點檢查
  - 實作複雜棋盤狀態的 step definitions
  - 確保 "Red moves the Elephant and its midpoint is blocked (Illegal)" scenario 通過
  - _Requirements: 6.3_

- [x] 8. 實作 Soldier (兵/卒) 相關 scenarios

- [x] 8.1 建立 Soldier 移動規則驗證方法

  - 實作 `is_legal_move_soldier` 方法處理未過河前進
  - 實作對應的 step definitions
  - 確保 "Red moves the Soldier forward before crossing the river (Legal)" scenario 通過
  - _Requirements: 7.1_

- [x] 8.2 實作 Soldier 未過河橫移的非法性驗證

  - 加強 `is_legal_move_soldier` 方法的過河前橫移檢查
  - 實作對應的 step definitions
  - 確保 "Red moves the Soldier and tries to move sideways before crossing (Illegal)" scenario 通過
  - _Requirements: 7.2_

- [x] 8.3 實作 Soldier 過河後橫移的合法性驗證

  - 加強 `is_legal_move_soldier` 方法的過河後橫移邏輯
  - 實作對應的 step definitions
  - 確保 "Red moves the Soldier sideways after crossing the river (Legal)" scenario 通過
  - _Requirements: 7.3_

- [x] 8.4 實作 Soldier 過河後後退的非法性驗證

  - 加強 `is_legal_move_soldier` 方法的後退檢查
  - 實作對應的 step definitions
  - 確保 "Red moves the Soldier and attempts to move backward after crossing (Illegal)" scenario 通過
  - _Requirements: 7.4_

- [x] 9. 實作勝負判定相關 scenarios

- [x] 9.1 實作吃掉將帥的勝利判定

  - 建立 `check_game_over` 和 `get_winner` 方法
  - 實作勝利判定的 step definitions
  - 確保 "Red captures opponent's General and wins immediately (Legal)" scenario 通過
  - _Requirements: 8.1, 8.3_

- [x] 9.2 實作吃掉非將帥棋子的遊戲繼續判定

  - 完善遊戲狀態管理邏輯
  - 實作對應的 step definitions
  - 確保 "Red captures a non-General piece and the game continues (Legal)" scenario 通過
  - _Requirements: 8.2, 8.3_

- [x] 10. 整合所有棋子規則到統一的移動驗證系統

- [x] 10.1 建立統一的移動驗證介面

  - 實作 `is_legal_move` 方法整合所有棋子規則
  - 重構 step definitions 使用統一介面
  - 確保所有現有 scenarios 仍然通過
  - _Requirements: 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1_

- [x] 10.2 實作完整的移動執行和狀態更新

  - 建立 `execute_move` 方法處理移動和吃子
  - 整合勝負判定到移動執行流程
  - 確保所有 scenarios 通過完整的移動流程測試
  - _Requirements: 8.1, 8.2, 8.3_

- [x] 11. 程式碼品質改善和最終驗證

- [x] 11.1 使用 Ruff 進行程式碼格式化和檢查

  - 執行 `ruff format` 格式化所有 Python 檔案
  - 執行 `ruff check` 檢查並修復程式碼問題
  - 確保程式碼符合 PEP 8 標準
  - _Requirements: 9.3_

- [x] 11.2 執行完整的 BDD 測試套件

  - 執行 `behave features/chess.feature` 確保所有 scenarios 通過
  - 產生測試報告和覆蓋率資訊

  - 驗證所有需求都有對應的測試覆蓋
  - _Requirements: 9.2, 9.4_

- [x] 11.3 最終程式碼重構和文檔更新

  - 重構重複程式碼和改善可讀性
  - 加入適當的程式碼註解和文檔字串
  - 確保所有測試在重構後仍然通過
  - _Requirements: 9.1, 9.2, 9.3, 9.4_
