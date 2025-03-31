from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from datetime import datetime,timedelta
import uuid
import qrcode 
from ..database.base import get_db 
from stbpass.models import * 


router = APIRouter()


@router.get("/{appointment_id}/approve")
async def approve_appointment(appointment_id:int,user:dict =Depends(require_role(["admin","Superadmin"]))):
    """ Admin API to approve or deny visitor entries """
    appointment = db.query(Appointment).filter_by(id=appointment_id,estate_id=user["managed_estate_id"]).first()
    if not appointment:
        raise HTTPException(status_code=404,detail="No appointments at the moment !!")
    appointment.status = "approved"
    appointment.admin_id = user["id"]
    db.commit()

    generate_pass(appointment)


def generate_pass(appointmrn)