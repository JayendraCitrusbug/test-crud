from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.application.dtos import VoiceAssessmentCreate, VoiceAssessmentUpdate, VoiceAssessmentRead
from src.application import services as app_services
from typing import List

# Assume get_db is available from a common dependencies module
from src.dependencies import get_db
from src.dependencies import get_redis

router = APIRouter(prefix="/voice-assessments", tags=["VoiceAssessment"])

@router.post("/", response_model=VoiceAssessmentRead)
def create_voice_assessment(
    obj_in: VoiceAssessmentCreate, db: Session = Depends(get_db)
):
    return app_services.create_voice_assessment(db, obj_in)

@router.get("/{id}", response_model=VoiceAssessmentRead)
def get_voice_assessment(id: str, db: Session = Depends(get_db)):
    obj = app_services.get_voice_assessment(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="VoiceAssessment not found")
    return obj

@router.get("/", response_model=List[VoiceAssessmentRead])
def get_voice_assessments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return app_services.get_voice_assessments(db, skip, limit)

@router.put("/{id}", response_model=VoiceAssessmentRead)
def update_voice_assessment(
    id: str, obj_in: VoiceAssessmentUpdate, db: Session = Depends(get_db)
):
    obj = app_services.update_voice_assessment(db, id, obj_in)
    if not obj:
        raise HTTPException(status_code=404, detail="VoiceAssessment not found")
    return obj

@router.delete("/{id}", response_model=bool)
def delete_voice_assessment(id: str, db: Session = Depends(get_db)):
    success = app_services.delete_voice_assessment(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="VoiceAssessment not found")
    return success 

# Redis-backed endpoints

@router.post("/redis/{id}", response_model=None)
def create_voice_assessment_redis(
    id: str, obj_in: VoiceAssessmentCreate, r = Depends(get_redis)
):
    app_services.create_voice_assessment_redis(r, id, obj_in)
    return {"success": True}

@router.get("/redis/{id}", response_model=VoiceAssessmentRead)
def get_voice_assessment_redis(id: str, r = Depends(get_redis)):
    obj = app_services.get_voice_assessment_redis(r, id)
    if not obj:
        raise HTTPException(status_code=404, detail="VoiceAssessment not found in Redis")
    return obj

@router.get("/redis/", response_model=List[VoiceAssessmentRead])
def get_voice_assessments_redis(r = Depends(get_redis)):
    return app_services.get_voice_assessments_redis(r)

@router.put("/redis/{id}", response_model=None)
def update_voice_assessment_redis(
    id: str, obj_in: VoiceAssessmentUpdate, r = Depends(get_redis)
):
    app_services.update_voice_assessment_redis(r, id, obj_in)
    return {"success": True}

@router.delete("/redis/{id}", response_model=None)
def delete_voice_assessment_redis(id: str, r = Depends(get_redis)):
    app_services.delete_voice_assessment_redis(r, id)
    return {"success": True} 
