# AGENTS.md — QuantumShield PQC Atlas

> 本文件是專案內所有 AI coding agents 與協作者的首要開發規則。開始新增或修改功能前，必須先閱讀此文件；若規則與任務衝突，應先指出衝突並以最小變更完成需求，不得默默破壞既有架構。

## 1. 專案目的與成功條件
- 建立繁體中文、適合初學者的後量子密碼學（PQC）教育知識庫。
- 提供可搜尋、可分類、可分享連結的知識文章。
- **核心目標：新增文章只需要修改 `data/articles.json`，不得為每篇文章手工複製 HTML 頁面。**
- 靜態網站可部署於 GitHub Pages 的 repository 子路徑，不使用後端或外部付費 API。
- 所有可見內容與資料需彼此一致，無空連結、無錯誤頁面。

## 2. 技術與限制
- 原生 HTML5、CSS3、JavaScript（ES2020+）；不使用 React、Vue、Node build step 或 CDN 套件。
- 文章資料為 UTF-8 JSON；所有路徑使用相對路徑，避免 GitHub Pages 專案子路徑錯誤。
- 不在客戶端放 API key、token、密碼或個人敏感資料。
- 不新增不必要的第三方追蹤、外部字體或分析腳本。

## 3. 專案目錄（單一職責）
```
/
├── AGENTS.md                 # AI 開發規則（本文件）
├── README.md                 # 使用、部署、展示說明
├── index.html                # 唯一 HTML 入口
├── assets/
│   ├── css/style.css         # 全站樣式
│   └── js/app.js             # 資料讀取、路由、卡片、文章模板、搜尋
├── data/articles.json        # 全部文章內容（內容唯一真實來源）
├── templates/article.example.json # 新文章欄位範例
└── scripts/validate.py       # 結構、命名、來源連結檢查
```

## 4. 網頁設計規範
- 主題：深藍色科技感、清爽、高對比、留白。
- 色彩統一使用 `assets/css/style.css` 中 `:root` CSS variables；主要背景 `#080e1d`，卡片 `#121d35`，重點青色 `#65e6ef`，紫色 `#b197ff`。
- 手機 560px 以下為單欄卡片；中間螢幕 2 欄，桌面 3 欄。
- 全站標題、導覽列、按鈕、分類標籤與文章均使用共用樣式。
- 主要介面與內容使用繁體中文；演算法、規格與程式術語保留官方英文縮寫。
- 所有互動元素需可使用鍵盤，表單具 aria-label；連結可辨識、文字有合理對比。

## 5. 文章資料 Schema（必填）
每篇文章在 `data/articles.json` 陣列中新增**一個物件**，不得刪除既有文章；格式請參考 `templates/article.example.json`。
- `slug`: 唯一識別碼，僅小寫英文字母、數字與連字號（`^[a-z0-9]+(?:-[a-z0-9]+)*$`）；建立後不能隨意變更，避免舊連結失效。
- `title`: 文章標題，繁體中文為主，不得為空。
- `category`: 分類，如「基礎概念」「核心演算法」「遷移實務」；優先沿用現有分類。新增分類前先確認必要性。
- `level`: 只可使用「入門」「中階」「實務」。
- `summary`: 30–100 字以內的清楚摘要，避免誇大安全性。
- `readingMinutes`: 1–30 的正整數。
- `sections`: 至少 2 個物件；每個具有 `heading`（非空字串）和 `paragraphs`（至少 1 個非空段落字串）。
- `sources`: 至少 1 個具有 `label` 與 `url` 的物件；URL 必須是 `https://` 開頭的可信官方來源。
- 禁止在 JSON 中嵌入 HTML、JavaScript 或 Markdown 表格；所有內容由共用模板轉為畫面。

## 6. 內容品質與資安規範
- 優先採用 NIST 官方文件（如 FIPS 203/204/205），並附上對應直接連結。
- 不臆造 NIST 規定、效能測試數字、安全性保證、發佈日期或研究結果；不確定時請明確寫出限制。
- 正確區分 KEM（金鑰封裝）、digital signature（數位簽章）與對稱加密；不得稱 ML-KEM 能直接加密一般檔案。
- 若使用 AI 產文，必須人工查核事實及來源，並修改為符合本網站程度與語氣的教學內容。
- 面向初學者，先定義術語，再說明用途，最後補充遷移／使用情境；保持短段落與明確標題。

## 7. AI 新增文章的標準操作流程
1. 先讀 `AGENTS.md`、`README.md`、`templates/article.example.json`、`data/articles.json`。
2. 檢查是否已有相同文章或相近分類，避免重複。
3. 找到可信來源，核對演算法名稱、標準編號與說法。
4. 使用 `templates/article.example.json` 的欄位，在 `data/articles.json` 最後新增文章物件。
5. 不改動 `index.html`、`app.js`、`style.css`，除非任務確實要求新增介面功能。
6. 執行 `python scripts/validate.py`，直到檢查通過。
7. 本機以 `python -m http.server 8000` 預覽首頁、分類搜尋、文章路由、參考來源與手機版。
8. 在回覆中列出新增 slug、變更檔案、資料來源與測試結果；若未測試必須明說。

## 8. AI 修改既有頁面的限制
- 遵守最小變更原則，不得因添加文章而重構整個網站。
- 任何新的文章顯示欄位都需同步更新：Schema、範例、validator、renderer、README 與本文件。
- 使用 `textContent` 或既有 `safe()` 逸出資料，不得將使用者輸入直接當作 HTML 執行。
- 修改搜尋或路由時，不得破壞既有 `#/article/{slug}` 連結。
- 變更 CSS 時使用既有變數，並測試 360px、768px、1280px 寬度。

## 9. 驗收清單（每次交付前確認）
- [ ] `python scripts/validate.py` 無錯誤
- [ ] 首頁正常顯示全部卡片；無搜尋結果時顯示提示
- [ ] 分類篩選與文字搜尋正常
- [ ] 所有 `#/article/{slug}` 文章頁能開啟
- [ ] 文章有官方來源連結，無虛構資料
- [ ] 手機版無水平溢出；鍵盤可用
- [ ] 不存在 API key、token、個資或非必要依賴
- [ ] GitHub Pages 子路徑部署後 CSS/JS/JSON 均可讀取

## 10. 可以直接交給 AI 的增量開發 Prompt
「請先閱讀本專案根目錄 AGENTS.md，遵循內容 Schema、來源規範和驗證流程。新增一篇『[文章主題]』文章，沿用既有網站風格與分類，優先只修改 data/articles.json。新增後執行 scripts/validate.py 並回報更動檔案、來源與驗證結果，不要修改其他既有文章。」
