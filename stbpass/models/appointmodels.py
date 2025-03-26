from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
import datetime
import uuid
from ..database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    visitor_name = Column(String, nullable=False)
    visitor_nin = Column(String, nullable=True)  # Temporarily stored, not permanent
    status = Column(String, default="pending")  # pending, approved, rejected
    visit_start = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    visit_end = Column(DateTime, nullable=False)  # Users set duration
    extended = Column(Boolean, default=False)  # Tracks if extension was requested

    user = relationship("User", back_populates="appointments")
    passes = relationship("Passcode", back_populates="appointment")  # Multiple passes per appointment


class Passcode(Base):
    __tablename__ = "passcodes"

    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=False)
    qr_code = Column(String, unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    expires_at = Column(DateTime, nullable=False)  # Pass expires when visit ends
    status = Column(String, default="active")  # active, expired, extended

    appointment = relationship("Appointment", back_populates="passes")  

    def extend_expiry(self, new_end_date: datetime.datetime):
        """ Extend pass validity if the visit duration is extended """
        if new_end_date > self.expires_at:
            self.expires_at = new_end_date
            self.status = "extended"

class ExpiredPass(Base):
    """ Store expired passes for auditing """
    __tablename__ = "expired_passes"

    id = Column(Integer, primary_key=True, index=True)
    pass_id = Column(Integer, ForeignKey("passcodes.id"), nullable=False)
    expired_at = Column(DateTime, default=datetime.datetime.utcnow)

    passcode = relationship("Passcode")  # Keep track of expired passes