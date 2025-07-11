from src.domain import services as domain_services
from src.application.dtos import VoiceAssessmentCreate, VoiceAssessmentUpdate, VoiceAssessmentRead
from sqlalchemy.orm import Session
from typing import List, Optional
from src.domain import redis_services
from redis import Redis

def create_voice_assessment(db: Session, obj_in: VoiceAssessmentCreate) -> VoiceAssessmentRead:
    obj = domain_services.create_voice_assessment(db, obj_in.dict())
    return VoiceAssessmentRead.from_orm(obj)

def get_voice_assessment(db: Session, id: str) -> Optional[VoiceAssessmentRead]:
    obj = domain_services.get_voice_assessment(db, id)
    if obj:
        return VoiceAssessmentRead.from_orm(obj)
    return None

def get_voice_assessments(db: Session, skip: int = 0, limit: int = 100) -> List[VoiceAssessmentRead]:
    objs = domain_services.get_voice_assessments(db, skip, limit)
    return [VoiceAssessmentRead.from_orm(obj) for obj in objs]

def update_voice_assessment(db: Session, id: str, obj_in: VoiceAssessmentUpdate) -> Optional[VoiceAssessmentRead]:
    db_obj = domain_services.get_voice_assessment(db, id)
    if not db_obj:
        return None
    obj_data = obj_in.dict(exclude_unset=True)
    updated = domain_services.update_voice_assessment(db, db_obj, obj_data)
    return VoiceAssessmentRead.from_orm(updated)

def delete_voice_assessment(db: Session, id: str) -> bool:
    db_obj = domain_services.get_voice_assessment(db, id)
    if not db_obj:
        return False
    domain_services.delete_voice_assessment(db, db_obj)
    return True

# Redis CRUD

def create_voice_assessment_redis(r: Redis, id: str, obj_in: VoiceAssessmentCreate) -> None:
    redis_services.create_voice_assessment_redis(r, id, obj_in.dict())

def get_voice_assessment_redis(r: Redis, id: str) -> Optional[VoiceAssessmentRead]:
    data = redis_services.get_voice_assessment_redis(r, id)
    if data:
        return VoiceAssessmentRead(**data)
    return None

def get_voice_assessments_redis(r: Redis) -> List[VoiceAssessmentRead]:
    data_list = redis_services.get_voice_assessments_redis(r)
    return [VoiceAssessmentRead(**data) for data in data_list]

def update_voice_assessment_redis(r: Redis, id: str, obj_in: VoiceAssessmentUpdate) -> None:
    data = obj_in.dict(exclude_unset=True)
    redis_services.update_voice_assessment_redis(r, id, data)

def delete_voice_assessment_redis(r: Redis, id: str) -> None:
    redis_services.delete_voice_assessment_redis(r, id) 