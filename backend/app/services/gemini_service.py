import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not configured")

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-3.5-flash-lite"


def generate_business_insights(metrics):
    prompt = f"""
You are a business analytics assistant.

Analyze the following sales data and provide useful business insights.

Business Metrics:
- Total Sales: ₹{metrics["total_sales"]}
- Total Profit: ₹{metrics["total_profit"]}
- Total Orders: {metrics["total_orders"]}
- Total Quantity Sold: {metrics["total_quantity"]}
- Profit Margin: {metrics["profit_margin"]}%

Monthly Sales:
{metrics["monthly_sales"]}

Sales by Region:
{metrics["regions"]}

Sales by Category:
{metrics["categories"]}

Top Products:
{metrics["products"]}

Provide:

1. Overall performance
2. Top performing region
3. Top performing category
4. Top performing product
5. Important sales trends
6. Two or three actionable business recommendations

Keep the response concise, clear, and easy to understand.
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Unable to generate AI insights: {str(e)}" 


def generate_chat_response(message, metrics):

    prompt = f"""
You are an AI business analytics assistant.

You answer questions using ONLY the business data provided below.

Business Metrics:

Total Sales:
₹{metrics["total_sales"]}

Total Profit:
₹{metrics["total_profit"]}

Total Orders:
{metrics["total_orders"]}

Total Quantity Sold:
{metrics["total_quantity"]}

Profit Margin:
{metrics["profit_margin"]}%

Monthly Sales:
{metrics["monthly_sales"]}

Sales by Region:
{metrics["regions"]}

Sales by Category:
{metrics["categories"]}

Top Products:
{metrics["products"]}


User Question:
{message}


Instructions:

- Answer the user's question clearly.
- Use the provided business data.
- Do not invent numbers.
- If the requested information is not available, say that the data is not available.
- Keep the answer concise.
- Use ₹ for Indian currency.
- When useful, explain the reasoning using the available data.
"""

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Unable to generate response: {str(e)}"