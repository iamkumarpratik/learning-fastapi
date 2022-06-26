from sqlalchemy import Column, String, ARRAY

from app.models.base_model import BaseModel, ModifiedMixin


class SurveyResponses(BaseModel, ModifiedMixin):
    __tablename__ = 'survey_responses'
    __table_args__ = ({'schema': 'response'},)

    full_name = Column(String(150), nullable=False)
    occupation = Column(String(150), nullable=False)
    favourite_tech = Column(String(150))
    skill = Column(String(150))
    current_competence_area = Column(String(256))
    linkedin_url = Column(String(256))
    certificates = Column(ARRAY(String))
