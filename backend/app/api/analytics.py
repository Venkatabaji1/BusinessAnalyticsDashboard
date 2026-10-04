from fastapi import APIRouter
from sqlalchemy import text

from app.database import engine


router = APIRouter(
    prefix="/api/analytics",
    tags=["Analytics"]
)


@router.get("/summary")
def get_summary():

    with engine.connect() as connection:

        result = connection.execute(
            text("""
                SELECT
                    SUM(sales) AS total_sales,
                    SUM(profit) AS total_profit,
                    COUNT(DISTINCT order_id) AS total_orders,
                    SUM(quantity) AS total_quantity
                FROM sales
            """)
        )

        row = result.fetchone()

    total_sales = row.total_sales or 0
    total_profit = row.total_profit or 0
    total_orders = row.total_orders or 0
    total_quantity = row.total_quantity or 0

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

@router.get("/monthly-sales")
def get_monthly_sales():

    with engine.connect() as connection:

        result = connection.execute(
            text("""
                SELECT
                    strftime('%Y-%m', order_date) AS month,
                    SUM(sales) AS sales
                FROM sales
                GROUP BY month
                ORDER BY month
            """)
        )

        rows = result.fetchall()

    return [
        {
            "month": row.month,
            "sales": row.sales
        }
        for row in rows
    ]


@router.get("/regions")
def get_sales_by_region():

    with engine.connect() as connection:

        result = connection.execute(
            text("""
                SELECT
                    region,
                    SUM(sales) AS sales
                FROM sales
                GROUP BY region
                ORDER BY sales DESC
            """)
        )

        rows = result.fetchall()

    return [
        {
            "region": row.region,
            "sales": row.sales
        }
        for row in rows
    ]


@router.get("/categories")
def get_sales_by_category():

    with engine.connect() as connection:

        result = connection.execute(
            text("""
                SELECT
                    category,
                    SUM(sales) AS sales
                FROM sales
                GROUP BY category
                ORDER BY sales DESC
            """)
        )

        rows = result.fetchall()

    return [
        {
            "category": row.category,
            "sales": row.sales
        }
        for row in rows
    ]


@router.get("/products")
def get_top_products():

    with engine.connect() as connection:

        result = connection.execute(
            text("""
                SELECT
                    product,
                    SUM(sales) AS sales
                FROM sales
                GROUP BY product
                ORDER BY sales DESC
                LIMIT 5
            """)
        )

        rows = result.fetchall()

    return [
        {
            "product": row.product,
            "sales": row.sales
        }
        for row in rows
    ]