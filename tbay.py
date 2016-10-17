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
    Column(('item_id'), Integer, ForeignKey('items.id'))
)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", secondary="user_bid_item_association", backref="items")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    item = relationship("Item", secondary="user_bid_item_association", backref="users")
    usersbids = relationship("Bid", backref="users")

class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)    


Base.metadata.create_all(engine)

def main():

    baseball = Item(name="Nolan_Ryan_Baseball", description="Nolan Ryan signed baseball")

    ben = User(username="ben", password="changeit")
    ben.item = [baseball,]
    
    will = User(username="will", password="changeit")
    baseball.bids = Bid(price=99.00, users=will)
    baseball.bids = Bid(price=109.00, users=will)
    
    fred = User(username="fred", password="changeit")
    baseball.bids = Bid(price=110.00, users=fred)
    baseball.bids = Bid(price=120.00, users=fred)
    
    baseball.bids = Bid(price=121.00, users=ben)
    baseball.bids = Bid(price=130.00, users=ben)

    session.add_all([ben, will, fred])
    session.commit()


if __name__ == "__main__":
    main()