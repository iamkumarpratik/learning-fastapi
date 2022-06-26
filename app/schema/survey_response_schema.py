from pydantic import BaseModel


class SurveyResponseSchema(BaseModel):
    full_name: str
    occupation: str
    favourite_tech: str | None = None
    skill: str | None = None
    current_competence_area: str | None = None
    linkedin_url: str | None = None
    certificates: list[str] | None = None

    class Config:
        orm_mode = True
