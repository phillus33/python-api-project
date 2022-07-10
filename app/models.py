"""Every model represents a table in the DB"""
from database import Base

# import database
from sqlalchemy import TIMESTAMP, Boolean, Column, String, Integer, text

# sqlalchemy model that defines the actual columns of the posts table in postgres
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
