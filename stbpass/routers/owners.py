from fastapi import APIRouter
from ..models import * 
from ..database import * 

router = APIRouter()


@router.post("/appointments/request")
def request_appointment(visitor_data: AppointmentRequest, user: dict = Depends(require_role(["owner"]))):
    """
    Owners submit a request for their visitor.
    """
    new_request = Appointment(
        visitor_name=visitor_data.visitor_name,
        visitor_email=visitor_data.visitor_email,
        owner_id=user["id"],
        estate_id=visitor_data.estate_id,
        start_date=visitor_data.start_date,
        end_date=visitor_data.end_date,
        status="pending"
    )
    db.add(new_request)
    db.commit()
    return {"message": "Appointment request submitted for approval."}

@router.post("/owners/view_houses/{id}")
def view_all_houses()