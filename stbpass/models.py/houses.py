from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.orm import relationship
import datetime
from ..database import Base

class Houses(Base):
    __tablename__ = 'Houses'

    id = Column(integer,primary_key=True,index=True)
    name = Column(String,max_length=50,nullable=False)
    address = Column(String,max_length=50,nullable=False)
    created_at = Column(DateTime,default =datetime.datetime.utcnow)


class Estates(Base):
    __tablename__ = 'Estates'

    id = Column(in)


