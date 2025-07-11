from .models import VoiceAssessment
from sqlalchemy.orm import Session
from typing import List, Optional

def create_voice_assessment(db: Session, obj_in: dict) -> VoiceAssessment:
    obj = VoiceAssessment(**obj_in)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_voice_assessment(db: Session, id: str) -> Optional[VoiceAssessment]:
    return db.query(VoiceAssessment).filter(VoiceAssessment.id == id).first()

def get_voice_assessments(db: Session, skip: int = 0, limit: int = 100) -> List[VoiceAssessment]:
    return db.query(VoiceAssessment).offset(skip).limit(limit).all()

def update_voice_assessment(db: Session, db_obj: VoiceAssessment, obj_in: dict) -> VoiceAssessment:
    for field, value in obj_in.items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_voice_assessment(db: Session, db_obj: VoiceAssessment) -> None:
    db.delete(db_obj)
    db.commit() 