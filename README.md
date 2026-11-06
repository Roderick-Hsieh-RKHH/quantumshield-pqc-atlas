# QuantumShield PQC Atlas

> 後量子密碼學互動式知識庫 — AGENTS.md 規則驅動的靜態網站。

## 專案簡介

網站以繁體中文介紹 PQC 基本觀念、NIST 標準、金鑰封裝、數位簽章與遷移規劃。除實際可瀏覽的網頁以外，本作業的核心是 **AGENTS.md**：它詳細規範 AI 要如何新增內容、命名檔案、維護一致風格並完成驗證。

## 已完成的功能
- 深色科技風格首頁、響應式卡片排版
- 知識文章共用模板、文章分類與關鍵字搜尋
- `#/article/{slug}` 直接分享文章路由
- 4 篇示範文章以及 NIST 官方參考來源
- `templates/article.example.json` 可複用內容範本
- `scripts/validate.py` 驗證文章 JSON 格式、slug 與來源
- `AGENTS.md` 定義 AI 開發流程、格式、樣式與驗收標準

## 如何在電腦預覽
請在專案資料夾開啟終端機：

```bash
python -m http.server 8000
```

瀏覽器開啟 http://localhost:8000 。請**不要雙擊 `index.html` 以 file:// 模式開啟**，因為瀏覽器可能阻止從本機檔案讀取 JSON。

執行資料格式檢查：

```bash
python scripts/validate.py
```

## GitHub Pages 部署
1. 在 GitHub 建立 Public repository（建議名稱 `quantumshield-pqc-atlas`）。
2. 將本專案**內容**上傳至 repository 根目錄（確認 `index.html`、`AGENTS.md` 位於最上層），commit 到 `main` 分支。
3. 開啟 GitHub repository → **Settings → Pages**。
4. 選擇 **Deploy from a branch**，Branch 設為 **main**，Folder 設為 **/(root)**，按 **Save**。
5. 發布完成後，網站網址通常為 `https://你的GitHub帳號.github.io/quantumshield-pqc-atlas/`（請以 GitHub Pages 實際顯示網址為準）。
6. 測試首頁、分類搜尋、文章頁、官方來源連結及手機版。

## 依照 AGENTS.md 擴充
例如要新增「什麼是密碼敏捷？」：請 AI 先讀 `AGENTS.md` 和 `templates/article.example.json`，在 `data/articles.json` 最後加上合法新文章物件，執行驗證後刷新網站即可。**不需新增 HTML 頁或手動改首頁卡片。**

推薦展示流程：展示 `AGENTS.md` → 請 AI 新增新文章 → 展示 JSON 變更 → 執行 `python scripts/validate.py` → 在網站搜尋新文章。

## 資料聲明
PQC 文章為教學整理，非正式部署或安全保證。參考 NIST 官方標準：[FIPS 203](https://csrc.nist.gov/pubs/fips/203/final)、[FIPS 204](https://csrc.nist.gov/pubs/fips/204/final)、[FIPS 205](https://csrc.nist.gov/pubs/fips/205/final)。

## 作業繳交說明（請先替換個人資訊及網址）

**繳交標題**：學校 學號 系級 姓名 QuantumShield PQC Atlas

**1. 專案簡介**：我建立了「QuantumShield PQC Atlas」，一個可搜尋和分類的後量子密碼學知識庫網站。網站介紹 PQC、ML-KEM、ML-DSA、SLH-DSA 及企業遷移流程，並透過 `AGENTS.md` 建立可重複使用的 AI 網頁開發規則。

**2. GitHub Repository 連結**：〔實際部署後填入〕

**3. 網頁連結**：〔GitHub Pages 啟用後填入〕

**4. AGENTS.md**：已存放在 Repository 根目錄，並定義專案目的、資料 Schema、設計規範、來源要求、AI 新增文章流程和驗收清單。

**5. 如何幫助 AI 繼續完成**：日後新增新頁面時，AI 只需閱讀 `AGENTS.md`，參考文章資料範本並在 `data/articles.json` 新增一個物件。首頁卡片、分類搜尋和文章頁就會自動出現，不必重做網頁。最後透過 `scripts/validate.py` 檢查格式、命名及參考來源，減少風格不一致及資料錯誤。
