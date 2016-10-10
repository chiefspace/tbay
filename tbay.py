<<<<<<< HEAD
""" tbay.py """

=======
>>>>>>> dd900a0e94c32fcbf9f2e49aaeb27461354f9fd8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


<<<<<<< HEAD
engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
=======
engine = create_engine('postgresql://vagrant:thinkful@localhost:5432/tbay')
>>>>>>> dd900a0e94c32fcbf9f2e49aaeb27461354f9fd8
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

<<<<<<< HEAD
from sqlalchemy import Table, Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship


user_bid_item_table = Table('user_bid_item_association', Base.metadata,
    Column(('user_id'), Integer, ForeignKey('users.id')),
    Column(('bid_id'), Integer, ForeignKey('bids.id')),
    Column(('item_id'), Integer, ForeignKey('items.id'))
)
=======
from sqlalchemy import Column, Integer, String, DateTime, Float
>>>>>>> dd900a0e94c32fcbf9f2e49aaeb27461354f9fd8

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
<<<<<<< HEAD
    auctioner = relationship("User", backref="items")
=======
>>>>>>> dd900a0e94c32fcbf9f2e49aaeb27461354f9fd8

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
<<<<<<< HEAD
    bidder = relationship("User", backref="bids")


Base.metadata.create_all(engine)

=======


Base.metadata.create_all(engine)
>>>>>>> dd900a0e94c32fcbf9f2e49aaeb27461354f9fd8
