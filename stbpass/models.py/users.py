from sqlalchemy import Column,Integer,String,ForiegnKey
from sqlalchemy.orm import relationship
from stbpass.models.base import Base
from stbpass.models.houses

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    email = Column(String,unique=True,nullable=False)
    role = Column(String,default="user") # user , admin , owners and superAdmin
    status =
    blacklist_status

    houses = relationship("House",back_populates="owner")
    appointments = relationship("Appointment",back_populates="user")

class Blacklist(Base):
    __tablename__ = "Blacklist"

    id = Column(Integer,primary_key=True,index=True)
