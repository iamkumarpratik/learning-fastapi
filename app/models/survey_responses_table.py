from sqlalchemy import Column, String

from app.models.base_model import BaseModel, ModifiedMixin


class SurveyResposes(BaseModel, ModifiedMixin):
    __tablename__ = 'survey_responses'

    full_name = Column(String(150), nullable=False)
    occupation = Column(String(150), nullable=False)
    favourite_tech = Column(String(150))
    skill = Column(String(150))
    current_competence_area = Column(String(256))
    linkedin_url = Column(String(256))
    certificates = Column(String(200))