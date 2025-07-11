from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from uuid import UUID
from datetime import datetime

class VoiceAssessmentCreate(BaseModel):
    deepgram_request_id: Optional[str] = None
    name: Optional[str] = None
    summary: Optional[str] = None
    speaker_identification: Optional[list] = Field(default_factory=list)
    assessment_score: Optional[dict] = Field(default_factory=dict)
    risk_assessment: Optional[list] = Field(default_factory=list)
    notes: Optional[dict] = None
    cpt_codes: Optional[list] = Field(default_factory=list)
    icd_codes: Optional[list] = Field(default_factory=list)
    overall_transcription: Optional[str] = None
    transcription_file_url: Optional[str] = None
    audio_file_url: Optional[str] = None
    session_type: Optional[str] = None
    note_template: Optional[str] = None
    status: Optional[str] = None
    language: Optional[str] = None
    patient_id: str
    interviewed_by: Optional[str] = None
    physician_type: Optional[str] = None
    duration: Optional[float] = 0

class VoiceAssessmentUpdate(BaseModel):
    deepgram_request_id: Optional[str] = None
    name: Optional[str] = None
    summary: Optional[str] = None
    speaker_identification: Optional[list] = None
    assessment_score: Optional[dict] = None
    risk_assessment: Optional[list] = None
    notes: Optional[dict] = None
    cpt_codes: Optional[list] = None
    icd_codes: Optional[list] = None
    overall_transcription: Optional[str] = None
    transcription_file_url: Optional[str] = None
    audio_file_url: Optional[str] = None
    session_type: Optional[str] = None
    note_template: Optional[str] = None
    status: Optional[str] = None
    language: Optional[str] = None
    patient_id: Optional[str] = None
    interviewed_by: Optional[str] = None
    physician_type: Optional[str] = None
    duration: Optional[float] = None

class VoiceAssessmentRead(BaseModel):
    id: str
    deepgram_request_id: Optional[str]
    name: Optional[str]
    summary: Optional[str]
    speaker_identification: Optional[list]
    assessment_score: Optional[dict]
    risk_assessment: Optional[list]
    notes: Optional[dict]
    cpt_codes: Optional[list]
    icd_codes: Optional[list]
    overall_transcription: Optional[str]
    transcription_file_url: Optional[str]
    audio_file_url: Optional[str]
    session_type: Optional[str]
    note_template: Optional[str]
    status: Optional[str]
    language: Optional[str]
    patient_id: str
    interviewed_by: Optional[str]
    physician_type: Optional[str]
    duration: Optional[float]

    class Config:
        orm_mode = True 