from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Passcode(Base):
    __tablename__ = "passcodes"

    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), unique=True)
    code = Column(String, unique=True, nullable=False)# QR code string
    

    appointment = relationship("Appointment", back_populates="passcode")