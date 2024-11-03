#!/usr/bin/python3
"""Definition of the State class with SQLAlchemy."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Создаем базовый класс для декларативных классов SQLAlchemy
Base = declarative_base()


class State(Base):
    """State class that links to the MySQL table `states`."""
    __tablename__ = 'states'

    # Определение столбцов
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
