from sqlalchemy.orm import Session
from app.models import StudentProfile
from app.schemas import StudentProfileCreate

def create_student_profile(db: Session, profile: StudentProfileCreate):
    db_profile = StudentProfile(
        name=profile.name,
        email=profile.email,
        phone=profile.phone,
        password=profile.password
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile
