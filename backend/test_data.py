from app.services.data_processor import (
    load_sales_data,
    get_basic_statistics,
    get_monthly_sales,
    get_sales_by_region,
    get_sales_by_category,
    get_top_products,
    get_top_customers
)


df = load_sales_data()


print("\n===== BASIC STATISTICS =====")

print(get_basic_statistics(df))


print("\n===== MONTHLY SALES =====")

print(get_monthly_sales(df))


print("\n===== SALES BY REGION =====")

print(get_sales_by_region(df))


print("\n===== SALES BY CATEGORY =====")

print(get_sales_by_category(df))


print("\n===== TOP PRODUCTS =====")

print(get_top_products(df))


print("\n===== TOP CUSTOMERS =====")

print(get_top_customers(df))