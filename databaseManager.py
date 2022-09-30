from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost/postgres", echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class SQL_Paint(Base):
        __tablename__ = "paint"

        id = Column(Integer, primary_key=True)
        name = Column(String[50])
        color = Column(String[50])
        type = Column(String[50])
        sizes = Column(String[50])
        prices = Column(String[50])
        area = Column(Float)

Base.metadata.create_all(engine)

def addItemToTable():
        paint1 = SQL_Paint(name="Dulux", color="White", type="Matt", sizes="2.5/5/10", prices="14/18/22", area="13")

        session.add(paint1)

        session.commit()


def addItemsManually():
        name = input("name ")
        color = input("color ")
        type = input("paint type ")
        sizes = input("paint sizes ")
        prices = input("paint prices ")
        area = input("area ")

        paint1 = SQL_Paint(name=name, color=color, type=type, sizes=sizes, prices=prices, area=area)

        session.add(paint1)

        session.commit()

def readDataOffTable():
        paints = session.query(SQL_Paint)
        for paint in paints:
                print(paint.name)
