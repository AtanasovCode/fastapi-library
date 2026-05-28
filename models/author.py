from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declared_attr, relationship
from database.database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates="author")