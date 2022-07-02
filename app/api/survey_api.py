from fastapi import APIRouter, HTTPException, Query, Body
from app.schema.survey_response_schema import SurveyResponseSchema
from app.queries.survey_responses_queries import SurveyResponseQueries
router = APIRouter()


@router.post('/survey/new')
def create_survey_response(survey: SurveyResponseSchema = Body(), username: str = Query(default=None, max_length=50)):

    try:
        survey_query = SurveyResponseQueries()
        survey_query.create_survey_response(survey)

    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    return {"survey":survey, "username": username}
