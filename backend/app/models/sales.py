from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(String, unique=True, nullable=False)
    order_date = Column(Date, nullable=False)

    customer = Column(String, nullable=False)
    product = Column(String, nullable=False)
    category = Column(String, nullable=False)
    region = Column(String, nullable=False)

    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)

    sales = Column(Float, nullable=False)
    profit = Column(Float, nullable=False)