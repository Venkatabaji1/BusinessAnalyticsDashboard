from sqlalchemy import text
from app.database import engine


with engine.connect() as connection:

    result = connection.execute(
        text("SELECT COUNT(*) FROM sales")
    )

    count = result.scalar()

    print(f"Total records in database: {count}")


    result = connection.execute(
        text("""
            SELECT
                order_id,
                customer,
                product,
                sales,
                profit
            FROM sales
            LIMIT 5
        """)
    )

    print("\n===== SAMPLE RECORDS =====")

    for row in result:
        print(row)