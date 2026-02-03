from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///../data/data.db")

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM employees WHERE senior = 1"))
    for row in result:
        print(row)
