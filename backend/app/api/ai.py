from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import text

from app.database import engine
from app.services.gemini_service import generate_business_insights
from app.services.gemini_service import generate_chat_response


router = APIRouter(
    prefix="/api/ai",
    tags=["AI Insights"]
)


class ChatRequest(BaseModel):
    message: str


def get_business_data():

    with engine.connect() as connection:

        # Summary
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

        summary = result.fetchone()

        total_sales = summary.total_sales or 0
        total_profit = summary.total_profit or 0
        total_orders = summary.total_orders or 0
        total_quantity = summary.total_quantity or 0

        profit_margin = (
            (total_profit / total_sales) * 100
            if total_sales > 0
            else 0
        )


        # Monthly sales
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

        monthly_sales = [
            {
                "month": row.month,
                "sales": row.sales
            }
            for row in result.fetchall()
        ]


        # Regions
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

        regions = [
            {
                "region": row.region,
                "sales": row.sales
            }
            for row in result.fetchall()
        ]


        # Categories
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

        categories = [
            {
                "category": row.category,
                "sales": row.sales
            }
            for row in result.fetchall()
        ]


        # Products
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

        products = [
            {
                "product": row.product,
                "sales": row.sales
            }
            for row in result.fetchall()
        ]


    return {
        "total_sales": total_sales,
        "total_profit": total_profit,
        "total_orders": total_orders,
        "total_quantity": total_quantity,
        "profit_margin": round(profit_margin, 2),
        "monthly_sales": monthly_sales,
        "regions": regions,
        "categories": categories,
        "products": products
    }


@router.get("/insights")
def get_business_insights():

    metrics = get_business_data()

    insights = generate_business_insights(metrics)

    return {
        "insights": insights
    }


@router.post("/chat")
def business_chat(request: ChatRequest):

    metrics = get_business_data()

    response = generate_chat_response(
        request.message,
        metrics
    )

    return {
        "response": response
    }