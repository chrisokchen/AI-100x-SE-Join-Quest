
任務 1 心得

-----
repo: https://github.com/chrisokchen/AI-100x-SE-Join-Quest/
language: Python
BDD framework: Behave
test framework: Pytest
IDE: VS Code + GitHub Copilot
-----

任務 1 : (/Join-Tasks/Task1/)


這是我第一次接觸 BDD，做任務前先買了 "BDD in Action 2ed" 來抱佛腳，也選了 Udemy 的 Gherkin 課先搞清楚。
認識到 BDD 在 AI 輔助軟體開發流程裡，至少有這些方面的助益：

    1. 需求發展階段：
        - Three Amigos 共同討論需求，確保需求明確且可測試。
        - 透過 Gherkin 語法，需求被轉化為可執行的測試案例，可以更清楚理解與定義需求，減少誤解的可能。
    2. 開發階段：
        - 以 features 產 steps，運行 TDD。
    3. 驗收階段：
        - features 就是 acceptance criteria，透過自動化測試，確保需求的實現符合預期。

這樣所謂的 "程式語言" 是否就可以 left shift 成 Gherkin？在公司裡 RD(需求發展) 跟 ReqM(需求管理) 兩個流程領域是我負責的 (汗顏！連 BDD 都不知？)，能這樣當然最好 (沒後面流程的事了 大誤! :-)

! 第一個生出的問題： 既然是 SBE，Scenario 例子如果沒有 cover 完全，是否可能產生出非唯一解？

以任務裡的 buy-one-get-one for cosmetics 邏輯為例，AI 實作時就來回迭代演了下面的內心小劇場：

    1. 第四個 scenario 按預期失敗：`Expected 口紅 quantity 3, got 4`; 這是因為我們的 buy-one-get-one 邏輯有問題。目前是「買幾個送幾個」，但正確的邏輯應該是「每買一個送一個」。讓我修正邏輯...
    2. 等等，我發現問題了。根據測試案例：
        - 買 2 個口紅，期望收到 3 個
        - 這意味著不是「買幾個送幾個」，而是「買 N 個，送 (N-1) 個」的概念
        讓我重新理解這個邏輯：買 2 個口紅，期望得到 3 個，這應該是「買 2 送 1」的概念。讓我重新實作...
    3. 等等，讓我重新看一下第三個 scenario 的邏輯：
        - 買 1 個口紅 + 1 個粉底液，期望得到 2 個口紅 + 2 個粉底液
        這表示每個商品買 1 個都送 1 個。所以正確的 buy-one-get-one 邏輯應該是：每個符合條件的商品，都會得到額外的贈品。讓我重新實作...
    4. 等等，這個邏輯還是不對。讓我重新分析測試案例：
        - 第三個 scenario： 買1個口紅 + 1個粉底液 → 得到2個口紅 + 2個粉底液，這表示每個商品都「買1送1」
        - 第四個 scenario： - 買2個口紅 → 得到3個口紅，這很奇怪，如果是「買1送1」，那買2個應該得到4個才對。
        讓我重新理解：可能 buy-one-get-one 的意思是「每個商品類型最多送一個」，不管買了多少...

當然，實際在正常狀況下 (雖然每奇數個可送1個也符合)，現有的 3 個 Scenarios 有覆蓋到規則的邊際狀況 (QA跟開發要加入的原因)，但在這個例子裡，AI 需要多次迭代才能理解正確的邏輯。這也顯示了 BDD / SBE 的一個重要特點：需求和規則可能需要多次澄清和迭代才能達到一致。

! 第二個問題: 非功能性需求 (NFRs) 能處理嗎？

應該說只要可量測，不是不行，但需要額外的注意和補充，至少這些量測應不是 Cucuber/Behave 的內建功能。

! 第三個問題： 後續的實作就真不管了嗎？

擴充 雙11促銷時，AI 原先產生 double11_service 可是裡頭沒東西，而是硬寫進 order_service 裡，經要求重構才把各種 promotion 一起分離開來。







! 以 BDD 開發時，feature 裡的 Scenario 例子如果沒有 cover 完全，是否可能產生出非唯一解?

在 BDD / Specification by Example 裡，Scenario 只是「**具體例子**」，本來就**不追求列舉全部情況**。若只寫了少數例子、又沒有把**規則（Rules）**說清楚，確實可能出現**多個彼此不同、但都能通過現有 Scenario 的實作**——也就是你說的「非唯一解」。([Gojko's blog][1], [martinfowler.com][2])


任務 3 心得

-----
repo: https://github.com/chrisokchen/AI-100x-SE-Join-Quest/
language: Python
BDD framework: Behave
test framework: Pytest
IDE: Kiro
-----

任務 3 : (/Join-Tasks/Task3/)

Kiro 的 Spec-Driven 與 BDD 有點像，但規格用 EARS（Easy Approach to Requirements Syntax)，比較整理了
