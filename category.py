from sqlalchemy import Column, VARCHAR
from sqlalchemy.orm import validates

from base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column('name', VARCHAR(length=200), nullable=False)
    description = Column('description', VARCHAR(length=200), nullable=True)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string!")
        if not name:
            raise ValueError("Name can't be null!")
        if len(name) > 200:
            raise ValueError("Name must have less than 200 characters.")
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError("Description must be a string!")
        if len(description) > 200:
            raise ValueError("Description must have less than 200 characters")
        return description


