# 🎮 Video Game Sales Analysis (VGChartz 2024)

## 🔎 Problem (What this solves)
Companies in gaming need to understand which platforms and titles drive sales, how sales change over time, and how critics’ ratings relate to game genres.
This analysis answers those questions using a VGChartz-style dataset.

## 📁 Dataset (What data is used)
- Source file: `vgchartz-2024.csv`
- Columns used:
  - `title`, `console`, `genre`
  - `release_date` (converted to datetime)
  - `na_sales`, `jp_sales`, `total_sales`
  - `critic_score`

## 🧠 Analysis (What I did)
1. Loaded the CSV and inspected structure (`head`, `shape`, `columns`, `dtypes`)
2. Converted `release_date` to datetime and extracted `release_year`
3. Checked missing years and filtered valid rows for yearly trends
4. Created a new feature: `na_jp_difference = na_sales - jp_sales`
5. Aggregations:
   - Top 10 consoles by total sales
   - Total sales by release year
   - Top 10 games by total sales
   - Average critic score by genre (NaNs ignored by `mean()`)
6. Visualizations:
   - Bar chart: Top 10 consoles by total sales
   - Line chart: Total sales by release year

## ✅ Outputs (What results it produces)
- Console ranking by total sales (Top 10)
- Sales trend by year (time series)
- Top-selling games list (Top 10)
- Genre ranking by average critic score

## 📊 Visualizations
If you export charts, add them into an `images/` folder and link them here:
- `images/top10_consoles.png`
- `images/sales_by_year.png`

Example:
![Top 10 Consoles](images/top10_consoles.png)
![Sales by Year](images/sales_by_year.png)

## ▶️ How to run
1. Install:
   ```bash
   pip install pandas matplotlib
