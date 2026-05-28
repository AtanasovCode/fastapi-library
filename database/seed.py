from database.database import Base, SessionLocal, engine
from models.category import Category
from models.author import Author
from models.book import Book


def seed():
    # Ensure database tables exist before inserting data
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        if db.query(Category).count() > 0:
            print("Database already seeded, skipping")
            return None

        categories = [
            Category(name="Science Fiction"),
            Category(name="Fantasy"),
            Category(name="History"),
            Category(name="Thriller"),
            Category(name="Horror"),
            Category(name="Romance"),
            Category(name="Comedy"),
            Category(name="Non-Fiction")
        ]

        db.add_all(categories)
        db.flush()

        authors = [
            Author(name="J.R.R. Tolkien"),
            Author(name="George R.R. Martin"),
            Author(name="J.K. Rowling"),
            Author(name="Stephen King"),
            Author(name="Agatha Christie"),
            Author(name="Isaac Asimov"),
            Author(name="Ernest Hemingway"),
            Author(name="Virginia Woolf"),
            Author(name="Mark Twain"),
            Author(name="Arthur Conan Doyle")
        ]

        db.add_all(authors)
        db.flush()

        books = [
            Book(
                name="The Fellowship of the Ring",
                price=19.99,
                quantity=10,
                pages=423,
                category_id=categories[1].id,
                author_id=authors[0].id
            ),
            Book(
                name="The Two Towers",
                price=19.99,
                quantity=8,
                pages=352,
                category_id=categories[1].id,
                author_id=authors[0].id
            ),
            Book(
                name="A Game of Thrones",
                price=24.99,
                quantity=15,
                pages=694,
                category_id=categories[1].id,
                author_id=authors[1].id
            ),
            Book(name="Harry Potter and the Sorcerer's Stone",
                 price=14.99,
                 quantity=20,
                 pages=309,
                 category_id=categories[1].id,
                 author_id=authors[2].id
                 ),
        ]

        db.add_all(books)
        db.commit()

    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
