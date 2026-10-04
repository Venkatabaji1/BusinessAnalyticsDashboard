import pandas as pd


def load_sales_data():
    file_path = r"E:\Business-Analytics-Dashboard\data\sales_data.csv"


    df = pd.read_csv(file_path)

    df["order_date"] = pd.to_datetime(df["order_date"])

    return df


def get_basic_statistics(df):
    total_sales = int(df["sales"].sum())
    total_profit = int(df["profit"].sum())
    total_orders = int(df["order_id"].nunique())
    total_quantity = int(df["quantity"].sum())

    profit_margin = (
        (total_profit / total_sales) * 100
        if total_sales > 0
        else 0
    )

    return {
        "total_sales": total_sales,
        "total_profit": total_profit,
        "total_orders": total_orders,
        "total_quantity": total_quantity,
        "profit_margin": round(profit_margin, 2)
    }


def get_monthly_sales(df):
    monthly_sales = (
        df.groupby(df["order_date"].dt.to_period("M"))["sales"]
        .sum()
        .reset_index()
    )

    monthly_sales["order_date"] = (
        monthly_sales["order_date"]
        .astype(str)
    )

    return monthly_sales.to_dict(orient="records")


def get_sales_by_region(df):
    region_sales = (
        df.groupby("region")["sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    return region_sales.to_dict(orient="records")


def get_sales_by_category(df):
    category_sales = (
        df.groupby("category")["sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    return category_sales.to_dict(orient="records")


def get_top_products(df, limit=5):
    product_sales = (
        df.groupby("product")["sales"]
        .sum()
        .sort_values(ascending=False)
        .head(limit)
        .reset_index()
    )

    return product_sales.to_dict(orient="records")


def get_top_customers(df, limit=5):
    customer_sales = (
        df.groupby("customer")["sales"]
        .sum()
        .sort_values(ascending=False)
        .head(limit)
        .reset_index()
    )

    return customer_sales.to_dict(orient="records")