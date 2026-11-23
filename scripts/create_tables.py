from app.database import Base, engine
import app.models  # To register the Department and Employee models in Base.metadata


def create_tables() -> None:
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()

"""
# Create Actual Table in MY_SQL Database. {Hit Must after Create create_table.py}
python -m scripts.create_tables

"""
"""
# Verification of the connection to MySQL from the .env file. Hit Terminal
python -c "from sqlalchemy import text; from app.database import engine; conn = engine.connect(); print(conn.execute(text('SELECT 1')).scalar()); conn.close()"


"""