# Reflection
# 1. 
#    In Excel I would open the file, filter the rows, and save a new copy by hand every time. In Python the script does it all in one run and I can
#    rerun it on a new file instantly. Excel is still easier for quickly looking at data or making a chart, while Python is better for repeating
#    the same steps on big files.
#
# 2. 
#    A store could log every return or refund on a register, with the time and amount, like at a customer service desk. Append mode is the right
#    tool because each new entry gets added to the end without erasing the earlier ones, so there is a full history.

import csv
from datetime import datetime

# -- Exercise 1: --

print("--- Exercise 1 ---")
with open("data/sales.csv", "r") as file:
    file.read()
print("data/sales.csv opened with no error")


# -- Exercise 2: --

print("\n--- Exercise 2 ---")
with open("data/sales.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# -- Exercise 3: --

print("\n--- Exercise 3 ---")
with open("data/sales.csv", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)


# -- Exercise 4: --

print("\n--- Exercise 4 ---")
total_revenue = 0
with open("data/sales.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")


# -- Exercise 5: --

print("\n--- Exercise 5 ---")
rows_read = 0
rows_written = 0
with open("data/sales.csv", newline="") as infile, \
        open("data/cleaned.csv", "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        rows_read += 1
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        if total > 100:
            writer.writerow([row[0], price, quantity, round(total, 2)])
            rows_written += 1
print(f"Rows in original: {rows_read}")
print(f"Rows written to data/cleaned.csv: {rows_written}")


# -- Exercise 6: --

print("\n--- Exercise 6 ---")
dict_total = 0
with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity
        dict_total += line_total
        print(f"{row['product']}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${dict_total:.2f}")
print(f"Matches Exercise 4: {round(dict_total, 2) == round(total_revenue, 2)}")

# csv.reader is quick for simple files because you only need the column positions,
# but csv.DictReader is better when columns have names, since row["price"] is easier to read and survives column reordering.


# -- Exercise 7: --

print("\n--- Exercise 7 ---")
summary = {}
with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        revenue = float(row["price"]) * int(row["quantity"])
        summary[row["product"]] = summary.get(row["product"], 0) + revenue
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")


# -- Exercise 8: --

print("\n--- Exercise 8 ---")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("data/run_log.txt", "a") as log:
    log.write(f"{timestamp} - Total revenue: ${total_revenue:.2f}\n")
print(f"Logged run to data/run_log.txt")