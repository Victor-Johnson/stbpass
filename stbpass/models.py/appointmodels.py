from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime
from stbpass.models.base import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    visitor_name = Column(Integer,nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    house_id = Column(Integer, ForeignKey("houses.id"))
    date_time = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default="Pending")  # Pending, Approved, Rejected

    user = relationship("User", back_populates="appointments")
    house = relationship("House", back_populates="appointments")
    passcode = relationship("Passcode", uselist=False, back_populates="appointment")