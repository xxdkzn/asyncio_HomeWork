import asyncio
import aiohttp
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

DATABASE_URL = 'postgresql+asyncpg://user:password@localhost/dbname'

Base = declarative_base()

class Character(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True)
    birth_year = Column(String)
    eye_color = Column(String)
    films = Column(Text)
    gender = Column(String)
    hair_color = Column(String)
    height = Column(String)
    homeworld = Column(String)
    mass = Column(String)
    name = Column(String)
    skin_color = Column(String)
    species = Column(Text)
    starships = Column(Text)
    vehicles = Column(Text)

async def fetch_character(session, character_id):
    async with session.get(f'https://swapi.dev/api/people/{character_id}/') as response:
        return await response.json()

async def save_character(session, character_data):
    character = Character(
        id=character_data['id'],
        birth_year=character_data['birth_year'],
        eye_color=character_data['eye_color'],
        films=', '.join(character_data['films']),
        gender=character_data['gender'],
        hair_color=character_data['hair_color'],
        height=character_data['height'],
        homeworld=character_data['homeworld'],
        mass=character_data['mass'],
        name=character_data['name'],
        skin_color=character_data['skin_color'],
        species=', '.join(character_data['species']),
        starships=', '.join(character_data['starships']),
        vehicles=', '.join(character_data['vehicles']),
    )
    
    async with session.begin():
        session.add(character)

async def main():
    engine = create_async_engine(DATABASE_URL, echo=True)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with aiohttp.ClientSession() as session:
        for character_id in range(1, 83):  # Кол-во персонажей которых вы хотите загрузить
            character_data = await fetch_character(session, character_id)
            await save_character(async_session(), character_data)

if __name__ == '__main__':
    asyncio.run(main())