class VoiceAssessment(Base, ActivityTracker):
    __tablename__ = "voice_assessment"
    __table_args__ = {"schema": app_settings.DATABASE["schema"]}

    id = Column(UUID(as_uuid=False), primary_key=True, default=uuid.uuid4)

    deepgram_request_id = Column(String, nullable=True)
    name = Column(
        String, nullable=False, default=f"Session {datetime.now().strftime('%m/%d/%Y')}"
    )
    summary = Column(String, nullable=True)
    speaker_identification = Column(ARRAY(JSON), nullable=False, default=[])
    assessment_score = Column(JSON, nullable=False, default={})
    risk_assessment = Column(ARRAY(String), nullable=False, default=[])
    notes = Column(JSON, nullable=True)
    cpt_codes = Column(ARRAY(JSON), nullable=False, default=[])
    icd_codes = Column(ARRAY(JSON), nullable=False, default=[])
    overall_transcription = Column(String, nullable=True)

    transcription_file_url = Column(String, nullable=True)
    audio_file_url = Column(String, nullable=True)

    session_type = Column(
        Enum(SessionTypeEnum),
        default=SessionTypeEnum.PSYCHIATRIC_INITIAL_EVALUATION,
    )
    note_template = Column(
        Enum(NoteTemplateEnum),
        default=NoteTemplateEnum.SOAP,
    )
    status = Column(
        Enum(StatusEnum),
        default=StatusEnum.TRANSCRIBING,
    )
    language = Column(
        Enum(LanguageEnum),
        default=LanguageEnum.EN,
    )

    patient_id = Column(
        UUID(as_uuid=False),
        ForeignKey(Patient.id),
        nullable=False,
    )

    interviewed_by = Column(String, nullable=True)

    physician_type = Column(
        Enum(PhysicianTypeEnum),
        default=PhysicianTypeEnum.OTHER,
    )

    duration = Column(Float, default=0)