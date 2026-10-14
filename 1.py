import pandas as pd

#Read all CSV files using Pandas.
customers = pd.read_csv("customers.csv")
orders    = pd.read_csv("orders.csv")
products  = pd.read_csv("products.csv")

print("customers.csv loaded:\n", customers)
print("\norders.csv loaded:\n", orders)
print("\nproducts.csv loaded:\n", products)

#Display record counts.
print(f"  Customers : {len(customers)} rows")
print(f"  Orders    : {len(orders)} rows")
print(f"  Products  : {len(products)} rows")

#IDENTIFY NULL (MISSING) VALUES.
print("Nulls in Customers:\n", customers.isnull().sum())
print("\nNulls in Orders:\n",   orders.isnull().sum())
print("\nNulls in Products:\n", products.isnull().sum())

#REMOVE DUPLICATE CUSTOMERS
print(f"  Rows before : {before}")
print(f"  Rows after  : {after}")
print(f"  Duplicates removed: {before - after}")

#FILL MISSING EMAILS WITH "Unknown"
customers["email"] = customers["email"].fillna("Unknown")
print("Emails after fill:\n", customers[["customer_id", "name", "email"]])

#STANDARDIZE COUNTRY NAMES TO UPPERCASE
customers["country"] = customers["country"].str.strip().str.upper()
print("Countries after standardization:\n", customers[["customer_id", "country"]])

#DATA QUALITY CHECKS
print("Unique countries:", customers["country"].unique())
print("\nCustomers with 'Unknown' email:",
      customers[customers["email"] == "Unknown"][["customer_id", "name"]])
print("\nDuplicate customer_ids remaining:",
      customers.duplicated(subset=["customer_id"]).sum())
print("\nFinal clean customers table:\n", customers)

#JOIN ORDERS WITH CUSTOMERS
orders_customers = orders.merge(customers, on="customer_id", how="inner")
print("Orders + Customers joined:\n", orders_customers)

#JOIN WITH PRODUCTS
full_data = orders_customers.merge(products, on="product_id", how="inner")
print("Columns in full dataset:", full_data.columns.tolist())
print("\nFull joined dataset:\n",
      full_data[["order_id", "name", "product_name", "quantity", "price", "order_date"]])

#CALCULATE SALES AMOUNT PER ORDER
full_data["sales_amount"] = full_data["quantity"] * full_data["price"]
print(full_data[["order_id", "name", "product_name", "quantity", "price", "sales_amount"]])



