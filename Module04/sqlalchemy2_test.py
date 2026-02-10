# This program uses the provided database named books.db located in the same directory as this program
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///Module04/books.db')
print(engine)

with engine.connect() as conn:
    result = conn.execute(text("SELECT title FROM book ORDER BY title"))
    cols = result.fetchall()

for col in cols:
    print(col)
