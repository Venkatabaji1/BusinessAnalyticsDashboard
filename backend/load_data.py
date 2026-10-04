from app.database import engine
from app.models.sales import Base, Sale
from app.services.data_processor import load_sales_data


# Make sure tables exist
Base.metadata.create_all(bind=engine)


# Load CSV data
df = load_sales_data()


# Convert Pandas records into SQLAlchemy objects
sales_records = []

for _, row in df.iterrows():
    sale = Sale(
        order_id=row["order_id"],
        order_date=row["order_date"].date(),
        customer=row["customer"],
        product=row["product"],
        category=row["category"],
        region=row["region"],
        quantity=int(row["quantity"]),
        unit_price=float(row["unit_price"]),
        sales=float(row["sales"]),
        profit=float(row["profit"])
    )

    sales_records.append(sale)


# Insert into database
with engine.begin() as connection:
    for sale in sales_records:
        connection.execute(
            Sale.__table__.insert(),
            {
                "order_id": sale.order_id,
                "order_date": sale.order_date,
                "customer": sale.customer,
                "product": sale.product,
                "category": sale.category,
                "region": sale.region,
                "quantity": sale.quantity,
                "unit_price": sale.unit_price,
                "sales": sale.sales,
                "profit": sale.profit
            }
        )


print(f"{len(sales_records)} sales records inserted successfully.")