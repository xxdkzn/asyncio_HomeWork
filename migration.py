from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://your_user:your_password@localhost/your_dbname'

Base = declarative_base()

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    birth_year = Column(String)
    eye_color = Column(String)
    films = Column(Text)  # Сохраняем названия фильмов как текст
    gender = Column(String)
    hair_color = Column(String)
    height = Column(String)
    homeworld = Column(String)
    mass = Column(String)
    name = Column(String)
    skin_color = Column(String)
    species = Column(Text)  # Сохраняем типы как текст
    starships = Column(Text)  # Сохраняем названия кораблей как текст
    vehicles = Column(Text)  # Сохраняем названия транспорта как текст

def main():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()
