from fastapi import APIRouter
from app.schema.survey_response_schema import SurveyResponseSchema
from app.queries.survey_responses_queries import SurveyResponseQueries
router = APIRouter()


@router.post('/survey/new', response_model=SurveyResponseSchema)
def create_survey_response(survey: SurveyResponseSchema):
    survey_query = SurveyResponseQueries()
    survey_query.create_survey_response(survey)

    return survey

