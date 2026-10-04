from app.database import engine
from app.models.sales import Base


Base.metadata.create_all(bind=engine)

print("Database created successfully.")