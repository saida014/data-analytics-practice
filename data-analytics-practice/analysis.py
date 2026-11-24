
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Подключение к базе данных
conn = sqlite3.connect("shop.db")

# 2. Получение данных из SQLite
df = pd.read_sql_query(
    "SELECT * FROM sales",
    conn
)

conn.close()

# Проверка данных
print("Данные из базы:")
print(df.head())

# Проверка наличия данных
if df.empty:
    print("В базе данных нет продаж!")
    exit()

# 3. Расчёт выручки
df["revenue"] = df["price"] * df["quantity"]

# 4. Общая выручка
total = df["revenue"].sum()

print("\nОбщая выручка магазина:", total, "тенге")

# 5. Общее количество проданных товаров
total_quantity = df["quantity"].sum()

print("Всего продано товаров:", total_quantity)

# 6. Выручка по товарам
products = df.groupby("product")["revenue"].sum()

print("\nВыручка по товарам:")
print(products)

# 7. Три товара с максимальной выручкой
top_products = products.sort_values(
    ascending=False
).head(3)

print("\nТОП-3 товара:")
print(top_products)

# 8. Количество продаж по товарам
product_quantity = df.groupby("product")["quantity"].sum()

print("\nКоличество проданных товаров:")
print(product_quantity)

# 9. Выручка по категориям
categories = df.groupby("category")["revenue"].sum()

print("\nВыручка по категориям:")
print(categories)

# 10. Создание папки charts
os.makedirs("charts", exist_ok=True)

# 11. Диаграмма №1 — выручка по товарам
plt.figure(figsize=(10, 6))

products.sort_values(ascending=False).plot(kind="bar")

plt.title("Выручка по товарам")
plt.xlabel("Товары")
plt.ylabel("Выручка, тенге")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("charts/revenue_by_products.png")
plt.show()
plt.close()

# 12. Диаграмма №2 — выручка по категориям
plt.figure(figsize=(8, 8))

categories.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Распределение выручки по категориям")
plt.ylabel("")
plt.tight_layout()

plt.savefig("charts/revenue_by_categories.png")
plt.show()
plt.close()

# 13. Диаграмма №3 — количество проданных товаров
plt.figure(figsize=(10, 6))

product_quantity.sort_values(ascending=False).plot(kind="bar")

plt.title("Количество проданных товаров")
plt.xlabel("Товары")
plt.ylabel("Количество, шт.")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("charts/quantity_by_products.png")
plt.show()
plt.close()

# 14. Выводы
print("\nАНАЛИЗ ПРОДАЖ")

print("1. Общая выручка магазина:", total, "тенге")

print("2. Общее количество проданных единиц:", total_quantity)

print("3. Самый прибыльный товар:",
      products.idxmax())

print("\nВсе три диаграммы сохранены в папке charts!")

print("Анализ завершён!")
