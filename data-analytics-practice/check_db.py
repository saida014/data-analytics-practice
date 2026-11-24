import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

# 1. Вывод всех записей
print("\nВСЕ ПРОДАЖИ")

cursor.execute("SELECT * FROM sales")

for row in cursor.fetchall():
    print(row)


# 2. Товары дороже 20 000 тенге
print("\nТОВАРЫ ДОРОЖЕ 20000 ТЕНГЕ")

cursor.execute("""
SELECT product, price
FROM sales
WHERE price > 20000
""")

for row in cursor.fetchall():
    print(row)


# 3. Товары определённой категории
print("\nКАТЕГОРИЯ: АКСЕССУАРЫ")

cursor.execute("""
SELECT product, price
FROM sales
WHERE category = 'Аксессуары'
""")

for row in cursor.fetchall():
    print(row)


# 4. Сортировка от дорогих к дешёвым
print("\nСОРТИРОВКА ПО ЦЕНЕ")

cursor.execute("""
SELECT product, price
FROM sales
ORDER BY price DESC
""")

for row in cursor.fetchall():
    print(row)


# 5. Количество записей
print("\nКОЛИЧЕСТВО ЗАПИСЕЙ")

cursor.execute("SELECT COUNT(*) FROM sales")

print(cursor.fetchone()[0])


# 6. Количество категорий
print("\nКАТЕГОРИИ ТОВАРОВ")

cursor.execute("""
SELECT DISTINCT category
FROM sales
""")

for row in cursor.fetchall():
    print(row[0])


conn.close()