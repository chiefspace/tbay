""" tbay.py """


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship


user_bid_item_table = Table('user_bid_item_association', Base.metadata,
    Column(('user_id'), Integer, ForeignKey('users.id')),
    Column(('bid_id'), Integer, ForeignKey('bids.id')),
    Column(('item_id'), Integer, ForeignKey('items.id'))
)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    item_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    user_id = relationship("User", secondary="user_bid_item_association", backref="items")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    user_id = relationship("Item", secondary="user_bid_item_association", backref="users")


class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    
    bid_id = Column(Integer, ForeignKey('items.id'), nullable=False)


Base.metadata.create_all(engine)

def main():
    ben = User(username="ben", password="changeit")
    will = User(username="will", password="changeit")
    fred = User(username="fred", password="changeit")
    session.add_all([ben, will, fred])
    session.commit()

    
if __name__ == "__main__":
    main()