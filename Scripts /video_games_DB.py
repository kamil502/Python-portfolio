import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
vg = pd.read_csv("vgchartz-2024.csv")

# Quick look
print(vg.head())
print(vg.shape)
print(vg.columns)
print(vg.dtypes)

# Convert date and create year
vg["release_date"] = pd.to_datetime(vg["release_date"])
vg["release_year"] = vg["release_date"].dt.year

# How many rows don't have a year
print(vg["release_year"].isna().sum())

# Keep only rows with year (for year trend)
vg_year = vg[vg["release_year"].notna()]

# Simple extra columns
vg["na_jp_difference"] = vg["na_sales"] - vg["jp_sales"]

# Top 10 consoles by total sales
sales_by_console = vg.groupby("console")["total_sales"].sum()
sales_by_console = sales_by_console.sort_values(ascending=False)
top_10_consoles = sales_by_console.head(10)
print(top_10_consoles)

# Total sales by year
sales_by_year = vg_year.groupby("release_year")["total_sales"].sum()
sales_by_year = sales_by_year.sort_index()
print(sales_by_year.head())

# Top 10 games by total sales
top_10_games = vg.sort_values("total_sales", ascending=False).head(10)
top_10_games = top_10_games[["title", "console", "genre", "total_sales", "release_date"]]
print(top_10_games)

# Avg critic score by genre (mean ignores missing values automatically)
avg_score_by_genre = vg.groupby("genre")["critic_score"].mean()
avg_score_by_genre = avg_score_by_genre.sort_values(ascending=False)
print(avg_score_by_genre)

# -----------------------
# Plots (at the end)
# -----------------------

plt.figure(figsize=(10, 5))
plt.bar(top_10_consoles.index, top_10_consoles.values)
plt.xticks(rotation=45)
plt.title("Top 10 Consoles by Total Sales")
plt.xlabel("Console")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(sales_by_year.index, sales_by_year.values)
plt.title("Total Sales by Release Year")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
